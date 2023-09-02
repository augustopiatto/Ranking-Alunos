from backend.models import Aluno, Atividade, Escola
from backend.services import student_svc
from backend.forms.student_forms import PostStudents, TopTenStudents
from django.core.exceptions import ValidationError
import pytest


def test_create_non_existent_student(db):
    name = "test"
    form = PostStudents(name=name)
    student_svc.post_students(form.name)

    assert Aluno.objects.filter(nome=name).exists()


def test_create_already_existent_student(db):
    Aluno.objects.create(nome="test")
    form = PostStudents(name="test")

    with pytest.raises(ValidationError) as exception:
        student_svc.post_students(form.name)
    assert exception.value.message == "O aluno já está cadastrado"


def test_get_students(db):
    response = student_svc.get_students()

    assert response == []

def test_get_top_three_students(db):
    student_1 = Aluno.objects.create(nome="test_1")
    student_2 = Aluno.objects.create(nome="test_2")
    student_3 = Aluno.objects.create(nome="test_3")
    student_4 = Aluno.objects.create(nome="test_4")

    data_school = Escola.objects.create(nome="data")
    tech_school = Escola.objects.create(nome="technology")

    data_school.alunos.add(student_1, student_2)
    tech_school.alunos.add(student_2, student_3, student_4)

    # student_1 - Data
    Atividade.objects.create(
        aluno=student_1,
        tipo="tasks",
        nota=1,
        escola=data_school
    )
    Atividade.objects.create(
        aluno=student_1,
        tipo="challenges",
        nota=2,
        escola=data_school
    )

    # student_2 - Data
    Atividade.objects.create(
        aluno=student_2,
        tipo="tasks",
        nota=3,
        escola=data_school
    )
    Atividade.objects.create(
        aluno=student_2,
        tipo="challenges",
        nota=4,
        escola=data_school
    )

    # student_2 - Tech
    Atividade.objects.create(
        aluno=student_2,
        tipo="tasks",
        nota=5,
        escola=tech_school
    )
    Atividade.objects.create(
        aluno=student_2,
        tipo="challenges",
        nota=6,
        escola=tech_school
    )

    # student_3 - Tech
    Atividade.objects.create(
        aluno=student_3,
        tipo="tasks",
        nota=7,
        escola=tech_school
    )
    Atividade.objects.create(
        aluno=student_3,
        tipo="challenges",
        nota=8,
        escola=tech_school
    )

    # student_4 - Tech
    Atividade.objects.create(
        aluno=student_4,
        tipo="tasks",
        nota=9,
        escola=tech_school
    )
    Atividade.objects.create(
        aluno=student_4,
        tipo="challenges",
        nota=10,
        escola=tech_school
    )

    response = student_svc.get_top_three_students()

    assert list(response.values_list("aluno", flat=True)) == [student_4.id, student_3.id, student_2.id]


@pytest.mark.parametrize("input, expected", [
    (
        ["data", "technology", "product"],
        ["test_11", "test_10", "test_9", "test_8", "test_7", "test_6", "test_5", "test_4", "test_3", "test_2"]
    ),
    (
        ["technology", "data", "product"],
        ["test_11", "test_10", "test_9", "test_8", "test_7", "test_6", "test_5", "test_4", "test_3", "test_2"]
    ),
    (
        ["product", "technology", "data"],
        ["test_11", "test_10", "test_9", "test_8", "test_7", "test_6", "test_5", "test_4", "test_3", "test_2"]
    ),
])
def test_get_top_ten_students(db, input, expected):
    student_1 = Aluno.objects.create(nome="test_1")
    student_2 = Aluno.objects.create(nome="test_2")
    student_3 = Aluno.objects.create(nome="test_3")
    student_4 = Aluno.objects.create(nome="test_4")
    student_5 = Aluno.objects.create(nome="test_5")
    student_6 = Aluno.objects.create(nome="test_6")
    student_7 = Aluno.objects.create(nome="test_7")
    student_8 = Aluno.objects.create(nome="test_8")
    student_9 = Aluno.objects.create(nome="test_9")
    student_10 = Aluno.objects.create(nome="test_10")
    student_11 = Aluno.objects.create(nome="test_11")
    student_12 = Aluno.objects.create(nome="test_12")
    student_13 = Aluno.objects.create(nome="test_13")

    first_school = Escola.objects.create(nome=input[0])
    second_school = Escola.objects.create(nome=input[1])
    third_school = Escola.objects.create(nome=input[2])

    first_school.alunos.add(
        student_1, student_2, student_3, student_4, student_5, student_6,
        student_7, student_8, student_9, student_10, student_11
    )
    second_school.alunos.add(student_12)
    third_school.alunos.add(student_13)

    for idx, student in enumerate(Aluno.objects.filter(escolas=first_school)):
        Atividade.objects.create(
            aluno=student,
            tipo="tasks",
            nota=idx + 1,
            escola=first_school
        )
        Atividade.objects.create(
            aluno=student,
            tipo="challenges",
            nota=idx + 2,
            escola=first_school
        )
    
    for idx, student in enumerate(Aluno.objects.filter(escolas=second_school)):
        Atividade.objects.create(
            aluno=student,
            tipo="tasks",
            nota=idx + 20,
            escola=second_school
        )
        Atividade.objects.create(
            aluno=student,
            tipo="challenges",
            nota=idx + 30,
            escola=second_school
        )
    
    for idx, student in enumerate(Aluno.objects.filter(escolas=third_school)):
        Atividade.objects.create(
            aluno=student,
            tipo="tasks",
            nota=idx + 40,
            escola=third_school
        )
        Atividade.objects.create(
            aluno=student,
            tipo="challenges",
            nota=idx + 50,
            escola=third_school
        )

    form = TopTenStudents(school=input[0])

    response = student_svc.get_top_ten_students(form.school)

    assert list(response.values_list("aluno__nome", flat=True)) == expected
