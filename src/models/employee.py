from src.config.db_settings import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Employee(Base):
    __tablename__ = "employees"

    username = Column(String, primary_key=True, index=True)
    password = Column(String)
    name = Column(String)
    company_position = Column(String)
    avatar = Column(String)

    skills = relationship("Skill", back_populates="employee")
