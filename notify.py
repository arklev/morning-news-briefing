import requests
import logging
from datetime import datetime
from config import NTFY_URL, NTFY_USER, NTFY_PASS, NOTIFICATION_CHANNEL, DISCORD_WEBHOOK_URL

def send_notification(message):
    if NOTIFICATION_CHANNEL == 'discord':
        return send_discord_notification(message)
    else:
        return send_ntfy_notification(message)

def send_ntfy_notification(message):
    try:
        auth = (NTFY_USER, NTFY_PASS) if NTFY_USER else None
        response = requests.post(
            NTFY_URL,
            data=message.encode('utf-8'),
            auth=auth,
            headers={
                "Title": "Morning News Briefing",
                "Priority": "default"
            }
        )
        response.raise_for_status()
        return True
    except Exception as e:
        logging.error(f'Failed to send ntfy notification: {e}')
        return False

def send_discord_notification(message):
    try:
        # Discord Embed structure for a professional look
        payload = {
            "username": "Ynet Tech Briefing",
            "avatar_url": "https://www.ynet.co.il/images/favicons/favicon.ico", # Updated icon URL
            "embeds": [
                {
                    "title": "📰 סיכום טכנולוגיה יומי",
                    "description": message,
                    "color": 3447003,  # Nice blue color
                    "footer": {
                        "text": "Ynet RSS Feed • Morning Briefing",
                    },
                    "timestamp": datetime.utcnow().isoformat()
                }
            ]
        }
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        return True
    except Exception as e:
        logging.error(f'Failed to send discord notification: {e}')
        return False
