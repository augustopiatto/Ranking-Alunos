from backend.services import grade_svc
from backend.forms.grade_forms import PostStudentGrade
from backend.models import Aluno, Atividade, Escola

def test_post_student_grade(db):
    student = Aluno.objects.create(nome="test")
    Escola.objects.create(nome="data")
    form = PostStudentGrade(student_id=student.id, school="data", grade=1.0, type="tasks")
    grade_svc.post_student_grade(form.student_id, form.school, form.grade, form.type)

    assert Atividade.objects.count() == 1
