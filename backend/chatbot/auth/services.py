from users.models import User
from datetime import datetime, timedelta
import jwt
from django.conf import settings
from django.contrib.auth import authenticate

class AuthService:
    @staticmethod
    def generate_jwt(user:User):
        payload = {
            "user_id": user.id,
            "email": user.email,
            "role": user.role,
            "exp": datetime.utcnow() + timedelta(days=7),
            "iat": datetime.utcnow(),
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        return token
    
    @staticmethod
    def authenticate_user(email, password):
        user = authenticate(email=email, password=password)
        if user:
            return AuthService.generate_jwt(user)
        return None