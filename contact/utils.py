import requests

def send_telegram_message(chat_id, message, bot_token):
    """
    Sends a message to a Telegram bot.
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML",  # optional for formatting
    }
    response = requests.post(url, data=data)
    return response.json()