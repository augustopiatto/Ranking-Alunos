from pydantic import BaseModel
from decimal import Decimal


class PostStudentGrade(BaseModel):
    student_id: int
    school: str
    grade: Decimal
    type: str
