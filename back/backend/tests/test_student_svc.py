from backend.models import Aluno, Atividade, Escola
from backend.services import student_svc


def test_get_top_three_students(db):
    student_1 = Aluno.objects.create(nome="teste_1")
    student_2 = Aluno.objects.create(nome="teste_2")
    student_3 = Aluno.objects.create(nome="teste_3")
    student_4 = Aluno.objects.create(nome="teste_4")

    data_school = Escola.objects.create(nome="DADOS")
    tech_school = Escola.objects.create(nome="TECNOLOGIA")

    data_school.alunos.add(student_1, student_2)
    tech_school.alunos.add(student_2, student_3, student_4)

    # student_1
    Atividade.objects.create(
        aluno=student_1,
        tipo="TAREFAS",
        nota=1,
        escola=data_school
    )
    Atividade.objects.create(
        aluno=student_1,
        tipo="DESAFIOS",
        nota=2,
        escola=data_school
    )

    # student_2 - Data
    Atividade.objects.create(
        aluno=student_2,
        tipo="TAREFAS",
        nota=3,
        escola=data_school
    )
    Atividade.objects.create(
        aluno=student_2,
        tipo="DESAFIOS",
        nota=4,
        escola=data_school
    )

    # student_2 - Tech
    Atividade.objects.create(
        aluno=student_2,
        tipo="TAREFAS",
        nota=5,
        escola=tech_school
    )
    Atividade.objects.create(
        aluno=student_2,
        tipo="DESAFIOS",
        nota=6,
        escola=tech_school
    )

    # student_3 - Tech
    Atividade.objects.create(
        aluno=student_3,
        tipo="TAREFAS",
        nota=7,
        escola=tech_school
    )
    Atividade.objects.create(
        aluno=student_3,
        tipo="DESAFIOS",
        nota=8,
        escola=tech_school
    )

    # student_4 - Tech
    Atividade.objects.create(
        aluno=student_4,
        tipo="TAREFAS",
        nota=9,
        escola=tech_school
    )
    Atividade.objects.create(
        aluno=student_4,
        tipo="DESAFIOS",
        nota=10,
        escola=tech_school
    )

    response = student_svc.get_top_three_students()

    assert list(response.values_list("aluno", flat=True)) == [4, 3, 2]
