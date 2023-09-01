from pydantic import BaseModel


class PostStudents(BaseModel):
    name: str
