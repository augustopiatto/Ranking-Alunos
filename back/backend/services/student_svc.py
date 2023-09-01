from backend.models import Atividade
from django.db.models import Avg


def get_students():
    return []


def post_students(name):
    pass


def get_top_three_students():
    ordered_students = (
        Atividade.objects.values("aluno", "escola")
        .annotate(grade_avg=Avg("nota"))
        .order_by("-grade_avg")
    )
    top_three_students = ordered_students[0:3]

    return top_three_students


def get_top_ten_students(school):
    return []
