from backend.models import Atividade, Escola
from django.core.exceptions import ObjectDoesNotExist, ValidationError


def post_student_grade(student_id, school, grade, type):
    try:
        school = Escola.objects.get(nome=school)
    except ObjectDoesNotExist:
        raise ValidationError("A escola informada não existe")

    Atividade.objects.create(
        tipo= type,
        nota=grade,
        aluno_id=student_id,
        escola=school
    )
