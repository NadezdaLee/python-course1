from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

# Загружаем переменные из .env
load_dotenv()

# Получаем данные автоматически
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

# Экранируем пароль (на случай спецсимволов)
encoded_password = quote_plus(password)

# Формируем строку подключения автоматически
DATABASE_URL = f"postgresql://{
    username}:{encoded_password}@{host}:{port}/{database}"

# Создаём движок
engine = create_engine(DATABASE_URL)

# Создаём фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Генератор для получения сессии БД"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
