#  DB access logic

from users.models import User


class UserRepository:
    
    def create_user(name: str, email: str)-> 'User':
        user = User(name=name, email=email)
        user.save()
        return user
    
    def get_all_users() -> list['User']:
        return list(User.objects.all())