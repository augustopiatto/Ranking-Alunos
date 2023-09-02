from backend.models import Aluno, Atividade, Escola
from django.core.management import call_command


def test_populating_db(db):
    assert Aluno.objects.count() == 0
    assert Escola.objects.count() == 0
    assert Atividade.objects.count() == 0

    call_command("dev_db")

    schools = Escola.objects.all()
    total_students = 0
    for school in schools:
        total_students += school.alunos.count()

    assert Aluno.objects.count() == 12
    assert Escola.objects.count() == 3
    assert total_students == 36
    assert Atividade.objects.count() == 108
    assert Atividade.objects.filter(tipo="tasks").count() == 36
    assert Atividade.objects.filter(tipo="challenges").count() == 36
    assert Atividade.objects.filter(tipo="projects").count() == 36
