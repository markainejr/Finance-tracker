import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:password1@localhost:5433/FinanceTrackerdb")
    SQLALCHEMY_TRACK_MODIFICATIONS = False



