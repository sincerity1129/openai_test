from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse

from chat_bot_assistant.controllers.chat_controller import ChatController

chat_controller = ChatController()


class AssistantChat(APIView):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        answer = chat_controller.user_question(
            "Tester", request.data.get("message")
        )
        return JsonResponse({"answer": str(answer)})