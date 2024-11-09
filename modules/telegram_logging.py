# modules/telegram_logging.py
import requests

def send_log(file_name, user_ip, user_agent, doc_type):
    bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
    chat_id = "YOUR_CHAT_ID"
    message = f"File: {file_name}\nIP: {user_ip}\nUser Agent: {user_agent}\nDokumen: {doc_type}"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)
