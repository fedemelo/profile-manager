from pydantic import BaseModel

class LoginResponse(BaseModel):
    username: str

class LoginCreate(BaseModel):
    username: str
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "johndoe",
                    "password": "password123",
                }
            ]
        }
    }