import requests
import logging
from config import NTFY_URL, NTFY_USER, NTFY_PASS

def send_notification(message):
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
        logging.error(f'Failed to send notification: {e}')
        return False
