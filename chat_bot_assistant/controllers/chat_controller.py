from openai import OpenAI
from dotenv import load_dotenv
import os

# from chat_bot_assistant.config import chat_cfg
from .common_controller import UserSessionController


class ChatController:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self.assistant_id = os.environ.get("ASSISTANTS_KEY")
        self.assistant = self.client.beta.assistants.retrieve(
            assistant_id=self.assistant_id,
        )

    def _chat_run(self, thread_id):
        run = self.client.beta.threads.runs.create_and_poll(
            thread_id=thread_id, assistant_id=self.assistant_id
        )
        messages = list(
            self.client.beta.threads.messages.list(thread_id=thread_id, run_id=run.id)
        )
        message_content = messages[0].content[0].text
        return message_content.value

    def user_question(self, user, content):
        user_session_info = UserSessionController.user_session_load()
        if user not in user_session_info:
            thread = self.client.beta.threads.create(
                messages=[
                    {
                        "role": "user",
                        "content": content,
                    }
                ]
            )
            UserSessionController.user_session_json(user, thread.id)
            return self._chat_run(thread.id)

        thread = self.client.beta.threads.messages.create(
            thread_id=user_session_info[user],
            role="user",
            content=content,
        )
        return self._chat_run(user_session_info[user])