from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from users.serializers import UserSerializer, UserCreateSerializer
from users.services import UserService
from auth.permissions import IsAdmin
from rest_framework.permissions import AllowAny, IsAuthenticated
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_permissions(self):
        """Permite el registro sin autenticación y protege las demás rutas."""
        if self.action == "create":  # Permitir solo el registro
            return [AllowAny()]
        return [IsAuthenticated(), IsAdmin()]  # Proteger las demás rutas

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        return UserSerializer
    
    def get_queryset(self):
        return UserService.find_all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"users": serializer.data}, status=status.HTTP_200_OK)  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserService.create_user(
            name=serializer.validated_data["name"],
            email=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
            role=serializer.validated_data.get("role", "USER")
        )
        return Response({"user":UserSerializer(user).data}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_user = UserService.update_user(
            user=user,
            name=serializer.validated_data.get("name"),
            role=serializer.validated_data.get("role")
        )
        return Response({"user":UserSerializer(updated_user).data})

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        UserService.delete_user(user)
        return Response(status=status.HTTP_204_NO_CONTENT)