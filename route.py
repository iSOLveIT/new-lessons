"""
    File containing the routes and view methods
"""

from app_example import app
from .models import User
from .schema import ValidateUser


@app.route('/')
def home():

    data = {
        "username": "joolie",
        "email": 'randy@example.com',
        "description": "I am testing things"
    }

    user = User(**data)
    print(user)

    user_data = ValidateUser.from_orm(user)
    print(user_data)




    # user.update()
    return "Hello World"

