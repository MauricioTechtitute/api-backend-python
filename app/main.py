from fastapi import FastAPI
from app.api.routers import health

app = FastAPI(title="API Backend Python")

app.include_router(health.router)







































# from fastapi import FastAPI
# from app.routers import courses

# app = FastAPI(
#     title="API Backend Python",
#     version="1.0.0"
# )

# @app.get("/")
# def health_check():
#     return {"status": "ok"}

# app.include_router(courses.router)































# from fastapi import FastAPI

# app = FastAPI(
#     title="API Backend Python",
#     version="1.0.0"
# )

# @app.get("/")
# def health_check():
#     return {"status": "ok"}

# @app.get("/courses")
# def get_courses():
#     return [
#         {"id": 1, "name": "Python Básico"},
#         {"id": 2, "name": "API REST con FastAPI"}
#     ]