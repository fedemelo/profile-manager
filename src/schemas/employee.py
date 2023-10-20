from pydantic import BaseModel


class EmployeeBase(BaseModel):
    name: str
    company_position: str
    avatar: str


class EmployeeCreate(EmployeeBase):
    username: str
    password: str


class Employee(EmployeeBase):
    username: str
    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "id": 1,
                "username": "johndoe",
                "password": "password123",
                "name": "John Doe",
                "company_position": "Software Engineer",
                "avatar": "https://example.com/image.png",
            }
        }
