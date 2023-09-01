from backend.views import student_view
from backend.models import Aluno
import json


def test_get_students(db, rf, mocker):
    student = Aluno.objects.create(nome="teste")
    mocker.patch("backend.services.student_svc.get_students", return_value=[student])
    request = rf.get("api/students/")
    response = student_view.students(request)

    assert response.status_code == 200
    assert json.loads(response.content) == [{"id": student.id, "name": student.nome}]


def test_post_students(db, rf, mocker):
    mocker.patch("backend.services.student_svc.post_students", return_value=None)
    request = rf.post("api/students/", {"name": "teste"}, content_type="application/json")
    response = student_view.students(request)

    assert response.status_code == 200
