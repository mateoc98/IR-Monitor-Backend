import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URL") or
        "postgresql://postgres:1234@localhost:5432/ir_monitor_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
