from pydantic import BaseModel


class SkillBase(BaseModel):
    name: str
    description: str
    level: float


class SkillCreate(SkillBase):
    pass


class Skill(SkillBase):
    id: int

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "id": 1,
                "name": "FastAPI",
                "description": "Proficiency in FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.",
                "level": 4.5,
            }
        }
