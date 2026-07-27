# This file defines the structure of a User
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int