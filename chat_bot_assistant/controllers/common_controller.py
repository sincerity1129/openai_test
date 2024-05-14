import json
from chat_bot_assistant.config.chat_cfg import user_session_path


class UserSessionController:
    def user_session_load():
        with open(user_session_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def user_session_json(user, thread):
        # JSON 파일 읽기
        with open(user_session_path, 'r') as file:
            data = json.load(file)
        data[user] = thread

        # JSON 파일 다시 쓰기
        with open(user_session_path, 'w') as file:
            json.dump(data, file, indent=4)