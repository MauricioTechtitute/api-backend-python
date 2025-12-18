from pydantic import BaseModel
from typing import Optional

class Course(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


class CourseCreate(BaseModel):
    name: str
    description: Optional[str] = None


class CoursePatch(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None




















# from pydantic import BaseModel

# class Course(BaseModel):
#     id: int
#     name: str