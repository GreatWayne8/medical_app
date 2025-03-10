import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://ai_user:your_secure_password@127.0.0.1/ai_services_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
