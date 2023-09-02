from backend.models import Aluno, Atividade, Escola
from django.db.models import Avg
from django.core.exceptions import ObjectDoesNotExist, ValidationError


def post_students(name):
    try:
        Aluno.objects.get(nome=name)
    except ObjectDoesNotExist: 
        Aluno.objects.create(nome=name)
        return

    raise ValidationError("O aluno já está cadastrado")


def get_students():
    students = Aluno.objects.all()

    return students


def get_top_three_students():
    ordered_students = (
        Atividade.objects.values("aluno__nome", "escola")
        .annotate(grade_avg=Avg("nota"))
        .order_by("-grade_avg")
    )
    top_three_students = ordered_students[0:3]

    return top_three_students


def get_top_ten_students(school):
    school_id = Escola.objects.get(nome=school).id
    ordered_students = (
        Atividade.objects.filter(escola_id=school_id)
        .values("aluno__nome", "escola")
        .annotate(grade_avg=Avg("nota"))
        .order_by("-grade_avg")
    )
    top_ten_students = ordered_students[0:10]

    return top_ten_students
