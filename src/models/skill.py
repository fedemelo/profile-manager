from config.db_settings import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Skill(Base):
    __tablename__ = "skills"

    name = Column(String, primary_key=True, index=True)
    description = Column(String)
    level = Column(Integer)
    employee_username = Column(String, ForeignKey("employees.username"))

    employee = relationship("Employee", back_populates="skills")
