from users.models import User

class UserService:
    
    @staticmethod
    def find_all():
        return User.objects.all()
    
    @staticmethod
    def create_user(name, email, password, role="USER"):
        return User.objects.create_user(name=name, email=email, password=password, role=role)

    @staticmethod
    def get_user_by_id(user_id):
        return User.objects.filter(id=user_id).first()

    @staticmethod
    def update_user(user, name=None, role=None):
        if name:
            user.name = name
        if role:
            user.role = role
        user.save()
        return user

    @staticmethod
    def delete_user(user):
        user.delete()