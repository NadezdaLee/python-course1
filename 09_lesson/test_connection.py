from database import engine
from sqlalchemy.exc import OperationalError

try:
    with engine.connect() as connection:
        print("Подключение к БД успешно установлено!")
except OperationalError as e:
    print(f"Ошибка подключения: {e}")
