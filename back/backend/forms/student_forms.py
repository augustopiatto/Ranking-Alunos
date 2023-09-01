from pydantic import BaseModel


class PostStudents(BaseModel):
    name: str


class TopTenStudents(BaseModel):
    school: str
