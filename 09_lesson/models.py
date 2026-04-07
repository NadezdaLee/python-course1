from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Используем старый синтаксис declarative_base()
# для совместимости с SQLAlchemy 1.4.x
# В будущем планируется переход на DeclarativeBase (SQLAlchemy 2.0+)
Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
