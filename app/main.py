from fastapi import FastAPI

app = FastAPI(
    title="API Backend Python",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/courses")
def get_courses():
    return [
        {"id": 1, "name": "Python Básico"},
        {"id": 2, "name": "API REST con FastAPI"}
    ]