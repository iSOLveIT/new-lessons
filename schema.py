"""
    File containing codes for pydantic
"""
from pydantic import BaseModel


class ValidateUser(BaseModel):

    username: str
    email: str
    description: str

    class Config:
        orm_mode = True
