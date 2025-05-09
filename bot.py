# archivo llamado bot.py

import os
import time
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

if __name__ == "__main__":
    while True:
        send_message("[ALERTA DE PRUEBA] Bot funcionando, Grego!")
        time.sleep(3600)  # Manda un mensaje cada 1 hora (después ajustamos)
