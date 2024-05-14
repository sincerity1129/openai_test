import json
from chat_bot_assistant.config.chat_cfg import user_session_path


class UserSessionController:
    def user_session_load():
        with open(user_session_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

if __name__ == "__main__":
    print(UserSessionController.user_session_load())
    print()