def env_key_add(api_key, key_name="ASSISTANTS_KEY", file_path=".env"):
    with open(file_path, "a") as file:
        # 새로운 키와 값을 파일에 추가
        file.write(f"\n{key_name}={api_key}")
    