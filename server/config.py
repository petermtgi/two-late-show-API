class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://late_user:mysecurepassword@localhost:5432/late_show_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "super-secret-key"
