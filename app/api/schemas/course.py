from pydantic import BaseModel


class Course(BaseModel):
    id: int
    name: str


class CourseCreate(BaseModel):
    name: str




























# from pydantic import BaseModel

# class Course(BaseModel):
#     id: int
#     name: str