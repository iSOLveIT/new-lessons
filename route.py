"""
    File containing the routes and view methods
"""

from app_example import app
from .models import User
from .schema import ValidateUser


@app.route('/')
def home():

    data = {
        "username": 'randy',
        "email": 'randy@example.com',
        "description": "I am testing things"
    }
    user_data = ValidateUser(**data)
    print(user_data)

    user = User(**user_data.dict())
    print(user)

    user.update()
    return "Hello World"

