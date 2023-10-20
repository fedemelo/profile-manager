from pydantic import BaseModel


class EmployeeBase(BaseModel):
    name: str
    company_position: str
    avatar: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "John Doe",
                    "company_position": "Software Engineer",
                    "avatar": "https://example.com/image.png",
                }
            ]
        }
    }


class EmployeeCreate(EmployeeBase):
    username: str
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


class Employee(EmployeeBase):
    username: str
    
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
