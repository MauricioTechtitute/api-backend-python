from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    COURSE_REPOSITORY: str = "memory"  # "memory" | "sqlite"
    SQLITE_DB_PATH: str = "app/data/courses.db"

settings = Settings()