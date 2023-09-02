from backend.forms.grade_forms import PostStudentGrade
from django.http import JsonResponse
from backend.services import grade_svc
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def post_student_grade(request):
    form = PostStudentGrade.model_validate(json.loads(request.body)['params'])
    grade_svc.post_student_grade(form.student_id, form.school, form.grade, form.type)

    return JsonResponse({})
