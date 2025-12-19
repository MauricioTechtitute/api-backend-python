from abc import ABC, abstractmethod
from typing import List, Optional

class CourseRepository(ABC):

    @abstractmethod
    def list(self) -> List[dict]: ...
    
    @abstractmethod
    def get(self, course_id: int) -> Optional[dict]: ...
    
    @abstractmethod
    def create(self, course: dict) -> dict: ...
    
    @abstractmethod
    def update(self, course_id: int, course: dict) -> dict: ...
    
    @abstractmethod
    def patch(self, course_id: int, data: dict) -> dict: ...
    
    @abstractmethod
    def delete(self, course_id: int) -> None: ...


































# from abc import ABC, abstractmethod
# from typing import List, Optional
# from app.models.course import Course

# class CourseRepository(ABC):

#     @abstractmethod
#     def list(self) -> List[Course]: ...

#     @abstractmethod
#     def get(self, course_id: int) -> Optional[Course]: ...

#     @abstractmethod
#     def create(self, course: Course) -> Course: ...

#     @abstractmethod
#     def update(self, course_id: int, course: Course) -> Course: ...

#     @abstractmethod
#     def patch(self, course_id: int, data: dict) -> Course: ...

#     @abstractmethod
#     def delete(self, course_id: int) -> None: ...
