from pydantic import BaseModel


class GetStudents(BaseModel):
    name: str
