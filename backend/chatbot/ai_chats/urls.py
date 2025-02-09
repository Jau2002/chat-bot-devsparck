from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ai_chats.views import AiChatView
urlpatterns = [
    path("ask/", AiChatView.as_view(), name="spark-ai"),
]