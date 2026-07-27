# api.py 
# This file contains all the endpoint function (acutal logic)
def get_user(user_id: int):
    '''Get information about a specifice user'''
    return {'user_id':user_id,
            'name':'John Doe',
            'email':f'user{user_id}@example.com',
            'status': 'activte'}
def update_user(user_id: int, name: str, email: str):
    """Update a user's information"""
    return {
        "user_id": user_id,
        "name": name,
        "email": email,
        "message": f"User {user_id} has been updated successfully"}

def list_users():
    """Get a list of all users"""
    return {
        "total_users": 3,
        "users": [
            {"user_id": 1, "name": "Alice"},
            {"user_id": 2, "name": "Bob"},
            {"user_id": 3, "name": "Charlie"}]}