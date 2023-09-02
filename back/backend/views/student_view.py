from django.http import JsonResponse
from backend.services import student_svc
from backend.serializers import student_serializers
from backend.forms.student_forms import PostStudents, TopTenStudents
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def students(request):
    if request.method == "POST":
        form = PostStudents.model_validate(json.loads(request.body)['params'])
        student_svc.post_students(form.name)

        return JsonResponse({})

    elif request.method == "GET":
        students = student_svc.get_students()
        serialized_students = [
            student_serializers.get_students_serializer(student) for student in students
        ] 
        return JsonResponse(serialized_students, safe=False)


def get_top_three_students(request):
    students = student_svc.get_top_three_students()
    serialized_students = [
        student_serializers.get_top_students_serializer(
            index, student
        ) for index, student in enumerate(students)
    ]

    return JsonResponse(serialized_students, safe=False)


def get_top_ten_students(request):
    form = TopTenStudents.model_validate(request.GET.dict())
    students = student_svc.get_top_ten_students(form.school)
    serialized_students = [
        student_serializers.get_top_students_serializer(
            index, student
        ) for index, student in enumerate(students)
    ] 

    return JsonResponse(serialized_students, safe=False)
