from pydantic import BaseModel
from typing import List
from src.schemas.skill import SkillResponse


class EmployeeBase(BaseModel):
    username: str
    name: str
    company_position: str
    avatar: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "johndoe",
                    "name": "John Doe",
                    "company_position": "Software Engineer",
                    "avatar": "https://example.com/image.png",
                }
            ]
        }
    }


class EmployeeCreate(EmployeeBase):
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "johndoe",
                    "password": "password123",
                    "name": "John Doe",
                    "company_position": "Software Engineer",
                    "avatar": "https://example.com/image.png",
                }
            ]
        }
    }


class EmployeeResponse(EmployeeBase):
    skills: List[SkillResponse]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "johndoe",
                    "name": "John Doe",
                    "company_position": "Software Engineer",
                    "avatar": "https://example.com/image.png",
                    "skills": [
                        {
                            "name": "Python",
                            "description": "A programming language",
                            "level": 4.8,
                        },
                        {
                            "name": "Docker",
                            "description": "A containerization platform",
                            "level": 4.6,
                        },
                    ],
                }
            ]
        }
    }
