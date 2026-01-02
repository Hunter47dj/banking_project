from users.repositories.user_repo import UserRepository

class UserService:
    
    def create_user(data):
        name = data.get('name')
        email = data.get('email')
        
        if not name:
            raise ValueError("Name is a required field.")
        if not email:
            raise ValueError("Email is a required field.")
        
        return UserRepository.create_user(name, email)
    
    
    def list_users():
        return UserRepository.get_all_users()