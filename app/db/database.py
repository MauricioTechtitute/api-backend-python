import sqlite3
from pathlib import Path
from app.core.settings import settings


def get_connection():
    db_path = Path(settings.SQLITE_DB_PATH)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(db_path)



























# import sqlite3
# from app.core.settings import settings

# def get_connection():
#     return sqlite3.connect(settings.SQLITE_DB_PATH)