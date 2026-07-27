# api.py — Contains the endpoint logic
from schemas import User


def create_user(user_data: User):
    # Do something with the user data
    return {"message": "User Created!", "user": user_data}
