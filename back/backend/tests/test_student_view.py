from backend.views import student_view
from backend.models import Aluno, Atividade, Escola
from django.db.models import Avg
import json


def test_get_students(db, rf, mocker):
    student = Aluno.objects.create(nome="teste")
    mocker.patch("backend.services.student_svc.get_students", return_value=[student])
    request = rf.get("api/students/")
    response = student_view.students(request)

    assert response.status_code == 200
    json_response = json.loads(response.content)
    assert json_response == [{"id": student.id, "name": student.nome}]


def test_post_students(db, rf, mocker):
    mocker.patch("backend.services.student_svc.post_students", return_value=None)
    request = rf.post("api/students/", {"params": {"name": "teste"}}, content_type="application/json")
    response = student_view.students(request)

    assert response.status_code == 200


def test_get_top_three_students(db, rf, mocker):
    student_1 = Aluno.objects.create(nome="teste_1")
    student_2 = Aluno.objects.create(nome="teste_2")

    data_school = Escola.objects.create(nome="DADOS")

    # student_1
    Atividade.objects.create(
        aluno=student_1,
        tipo="TAREFAS",
        nota=2,
        escola=data_school
    )
    # student_2
    Atividade.objects.create(
        aluno=student_2,
        tipo="TAREFAS",
        nota=1,
        escola=data_school
    )
    service_response = (
        Atividade.objects.values("aluno", "escola", "aluno__nome")
        .annotate(grade_avg=Avg("nota"))
        .order_by("-grade_avg")
    )[0:3]

    mocker.patch(
        "backend.services.student_svc.get_top_three_students",
        return_value=service_response
    )

    request = rf.get("api/top-three-students/")
    response = student_view.get_top_three_students(request)

    assert response.status_code == 200
    json_response = json.loads(response.content)
    assert json_response == [
        {"idx": 1, "name": student_1.nome, "final_score": "2.00"},
        {"idx": 2, "name": student_2.nome, "final_score": "1.00"}
    ]


def test_get_top_ten_students(db, rf, mocker):
    # Serializer ja foi testado no test_get_top_three_students
    mocker.patch("backend.services.student_svc.get_top_ten_students", return_value=[])

    request = rf.get("api/top-ten-students/", {"school": "teste"})
    response = student_view.get_top_ten_students(request)

    assert response.status_code == 200
