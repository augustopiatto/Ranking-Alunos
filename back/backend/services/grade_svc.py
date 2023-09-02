from backend.models import Atividade, Escola


def post_student_grade(student_id, school, grade, type):
    school = Escola.objects.get(nome=school)
    Atividade.objects.create(
        tipo= type,
        nota=grade,
        aluno_id=student_id,
        escola=school
    )
