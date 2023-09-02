from backend.forms.grade_forms import PostStudentGrade
from django.http import JsonResponse
from backend.services import grade_svc


def post_student_grade(request):
    form = PostStudentGrade.model_validate_json(request.body)
    grade_svc.post_student_grade(form.student_id, form.school, form.grade, form.type)

    return JsonResponse({})
