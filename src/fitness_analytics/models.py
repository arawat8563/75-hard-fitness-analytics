from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date, Boolean, Numeric, ForeignKey


Base = declarative_base()

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True)
    exercise_name = Column(String(100), nullable=False)
    muscle_group = Column(String(50))