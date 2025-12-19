import sqlite3
from app.core.settings import settings

def get_connection():
    return sqlite3.connect(settings.SQLITE_DB_PATH)