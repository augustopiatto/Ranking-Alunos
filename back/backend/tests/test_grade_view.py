from backend.views import grade_view
from backend.models import Aluno


def test_post_student_grade_view(db, rf, mocker):
    mocker.patch("backend.services.grade_svc.post_student_grade", return_value=None)
    student = Aluno.objects.create(nome="test")
    request = rf.post(
        "api/grade/",
        {"student_id": student.id, "school": "data", "grade": 1.0, "type": "tasks"},
        content_type="application/json"
    )
    response = grade_view.post_student_grade(request)

    assert response.status_code == 200
