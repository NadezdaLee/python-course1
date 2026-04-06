import pytest
from sqlalchemy.orm import sessionmaker
from database import engine
from models import Base, Student

# Настройка тестовой БД
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def db_session():
    # Создаём таблицы перед тестом
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        # Очищаем данные после теста
        session.query(Student).delete()
        session.commit()
        session.close()
        # Удаляем таблицы
        Base.metadata.drop_all(bind=engine)


def test_create_student(db_session):
    """Тест добавления студента"""
    # Данные для создания
    student_data = {
        "name": "Иван Иванов",
        "email": "ivan@example.com"
    }

    # Создаём студента
    student = Student(**student_data)
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    # Проверяем, что студент создан
    assert student.id is not None
    assert student.name == student_data["name"]
    assert student.email == student_data["email"]

    # Удаляем созданного студента
    db_session.delete(student)
    db_session.commit()


def test_update_student(db_session):
    """Тест изменения студента"""
    # Сначала создаём студента
    original_student = Student(
        name="Пётр Петров",
        email="petr@example.com"
    )
    db_session.add(original_student)
    db_session.commit()
    db_session.refresh(original_student)

    # Обновляем данные
    updated_data = {
        "name": "Пётр Сидоров",
        "email": "sidorov@example.com"
    }
    original_student.name = updated_data["name"]
    original_student.email = updated_data["email"]
    db_session.commit()

    # Проверяем обновление
    updated_student = db_session.query(
        Student).filter(Student.id == original_student.id).first()
    assert updated_student.name == updated_data["name"]
    assert updated_student.email == updated_data["email"]

    # Удаляем студента
    db_session.delete(updated_student)
    db_session.commit()


def test_delete_student(db_session):
    """Тест удаления студента"""
    # Создаём студента для удаления
    student_to_delete = Student(
        name="Алексей Алексеев",
        email="alex@example.com"
    )
    db_session.add(student_to_delete)
    db_session.commit()
    db_session.refresh(student_to_delete)

    # Сохраняем ID перед удалением
    student_id = student_to_delete.id

    # Удаляем студента
    db_session.delete(student_to_delete)
    db_session.commit()

    # Проверяем отсутствие студента в БД
    deleted_student = db_session.query(
        Student). filter(Student.id == student_id).first()
    assert deleted_student is None
