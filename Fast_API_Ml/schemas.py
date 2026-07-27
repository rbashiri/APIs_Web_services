# create schemas# schemas.py: Data rules

from pydantic import BaseModel , Field
from typing import Optional # make a field optional 
class UserCreats(BaseModel):
    '''Schema for creating a new user'''
    name: str = Field (min_length=1, max_length= 50)
    email : str =Field (min_length=3, max_length= 100)
    age : int = Field(ge=0, le=150)
    bio: Optional[str] = None
    phone: Optional[str]= None # # Optional field with default None
    #This model says: 
    # "A User must have a name (string), email (string), and age (integer)."

class UserUpdate(BaseModel):
    """Schame for updating an existing user"""
    name: Optional[str] = Field(None, min_length=1, max_length=50)
    email: Optional[str] = Field(None, min_length=3, max_length=100)
    age: Optional[int] = Field(None, ge=0, le=150)
    bio: Optional[str] = None

class UserResponse(BaseModel):
    """Schema for user response"""
    user_id : int 
    name:str
    email : str
    age: int 
    bio: Optional[str]=None
    status: str= 'active'
