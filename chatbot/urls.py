from django.contrib import admin
from django.urls import path
from chat_bot_assistant.views import AssistantChat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat-test', AssistantChat.as_view()),
]
