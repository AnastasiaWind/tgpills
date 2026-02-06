import os
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": "Ежедневный текст",
        "reply_markup": {
            "inline_keyboard": [[{"text": "Нажми меня", "callback_data": "btn_1"}]]
        },
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    send_message()
