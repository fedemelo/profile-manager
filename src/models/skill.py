from src.config.db_settings import Base
from sqlalchemy import Column, Float, String, ForeignKey
from sqlalchemy.orm import relationship


class Skill(Base):
    __tablename__ = "skills"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    level = Column(Float)

    employee_username = Column(String, ForeignKey("employees.username"))

    employee = relationship("Employee", back_populates="skills")

    