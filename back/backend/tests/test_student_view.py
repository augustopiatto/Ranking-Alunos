from backend.views import student_view


def test_get_students(rf, mocker):
    mocker.patch("backend.services.student_svc.get_students", return_value=[])
    request = rf.get("api/students/")
    response = student_view.students(request)

    assert response.status_code == 200
