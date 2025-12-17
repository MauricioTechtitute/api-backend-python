from fastapi import FastAPI
from app.api.routers import health_router, courses_router

app = FastAPI(
    title="API Backend Python",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(courses_router)

@app.get("/")
def root():
    return {
        "service": "API Backend Python",
        "status": "running"
    }




























# from fastapi import FastAPI
# from app.api.routers.health import router as health_router
# from app.api.routers.courses import router as courses_router

# app = FastAPI(
#     title="API Backend Python",
#     version="1.0.0"
# )

# app.include_router(health_router)
# app.include_router(courses_router)

# @app.get("/")
# def root():
#     return {
#         "service": "API Backend Python",
#         "status": "running"
#     }

































# from fastapi import FastAPI
# from app.api.routers.health import router as health_router

# app = FastAPI(
#     title="API Backend Python",
#     version="1.0.0"
# )

# app.include_router(health_router)

# @app.get("/")
# def root():
#     return {
#         "service": "API Backend Python",
#         "status": "running"
#     }

# @app.get("/courses")
# def get_courses():
#     return [
#         {"id": 1, "name": "Python Básico"},
#         {"id": 2, "name": "API REST con FastAPI"}
#     ]