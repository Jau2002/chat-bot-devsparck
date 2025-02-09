from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ai_chats.services import AiChatService

class AiChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_message = request.data.get("message")
        if not user_message:
            return Response({"error": "Debes enviar un mensaje"}, status=400)

        response = AiChatService.ask_ai(user_message)
        return Response({"response": response})