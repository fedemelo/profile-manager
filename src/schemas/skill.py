from pydantic import BaseModel


class SkillBase(BaseModel):
    name: str
    description: str
    level: float

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "FastAPI",
                    "description": "Proficiency in FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.",
                    "level": 4.5,
                },
                {
                    "name": "React",
                    "description": "Proficiency in React, a JavaScript library for building user interfaces.",
                    "level": 4.0,
                },
            ]
        }
    }


class SkillCreate(SkillBase):
    pass


class SkillResponse(SkillBase):
    pass
