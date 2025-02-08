from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from auth.services import AuthService
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

User = get_user_model()

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        token = AuthService.authenticate_user(email, password)
        if token:
            return Response({"token": token}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):
    def post(self, request):
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)