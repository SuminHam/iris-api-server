import hashlib
import time
import secrets


def generate_api_key(user_id):
    salt = secrets.token_hex(16)
    timestamp = str(int(time.time()))
    pre_key = f"{user_id}{timestamp}{salt}"
    api_key = hashlib.sha256(pre_key.encode()).hexdigest()
    return api_key


print(generate_api_key("12"))
