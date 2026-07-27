# api.py — Contains the endpoint logic

from schemas import UserCreats, UserUpdate , UserResponse


def create_user(user_data:UserCreats):
    """Create a new user with validated data"""
    # In a real app, you'd save this to a database
    # For now, we'll just return the data with an ID
    return UserResponse(
        user_id=123,
        name=user_data.name,
        email=user_data.email,
        age=user_data.age,
        bio=user_data.bio,
        status="active"
    )

def get_user(user_id: int):
    """Get information about a specific user"""
    return UserResponse(
        user_id=user_id,
        name="John Doe",
        email="john.doe@example.com",
        age=30,
        bio="Software developer",
        status="active")
def update_user(user_id: int, user_data: UserUpdate):
    """Update a user's information with validated data"""
    # In a real app, you'd update the database
    # For now, we'll return updated data
    return {
        "user_id": user_id,
        "updated_fields": user_data.model_dump(exclude_none=True),
        "message": f"User {user_id} has been updated successfully"
    }

def list_users():
    """Get a list of all users"""
    return {
        "total_users": 3,
        "users": [
            UserResponse(user_id=1, name="Alice", email="alice@example.com", age=25),
            UserResponse(user_id=2, name="Bob", email="bob@example.com", age=30),
            UserResponse(user_id=3, name="Charlie", email="charlie@example.com", age=35)
        ]
    }