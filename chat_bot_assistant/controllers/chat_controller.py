from openai import OpenAI
from dotenv import load_dotenv
import json
import os

from chat_bot_assistant.config import chat_cfg
from .common_controller import env_key_add
load_dotenv(override=True)

class ChatController:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        load_dotenv(override=True)
        if os.environ.get("ASSISTANTS_KEY") == None:
            # basic chatbot setting
            self.assistant = self.client.beta.assistants.create(
                name=chat_cfg.chat_name,
                instructions=chat_cfg.instruction,
                tools=[{"type": "file_search"}],
                model=chat_cfg.model,
            )
            env_key_add(self.assistant.id)
            self.assistant_id = os.environ.get("ASSISTANTS_KEY")
        else:
            self.assistant_id = os.environ.get("ASSISTANTS_KEY")
        self.assistant = self.client.beta.assistants.update(
            assistant_id=self.assistant_id,
        )

    def _chat_run(self, thread):
        run = self.client.beta.threads.runs.create_and_poll(
            thread_id=thread.id, assistant_id=self.assistant_id
        )
        messages = list(
            self.client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id)
        )
        message_content = messages[0].content[0].text
        return message_content.value


    def user_question(self, user, content):
        if thread.user != user:
            thread = self.client.beta.threads.create(
                messages=[
                    {
                        "role": "user",
                        "content": content,
                    }
                ]
            )
            env_key_add(thread.id, user)
        else:
            thread = self.client.beta.threads.messages.create(
                thread_id=thread.id,
                role="user",
                content=content,
            )
        return self._chat_run(thread)
