from backend.views import student_view


def test_get_students(mocker):
    response = student_view.students()

    assert response.status_code == 200
