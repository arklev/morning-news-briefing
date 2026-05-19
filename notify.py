import requests
import logging
from datetime import datetime
from config import NTFY_URL, NTFY_USER, NTFY_PASS, NOTIFICATION_CHANNEL, DISCORD_WEBHOOK_URL

def send_notification(results):
    if NOTIFICATION_CHANNEL == 'discord':
        return send_discord_notification(results)
    else:
        # For ntfy, just join summaries
        if isinstance(results, list):
            message = "\n\n".join([f"• {r['summary']} [קרא עוד]({r['link']})" for r in results])
        else:
            message = results
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

def send_discord_notification(results):
    if not isinstance(results, list):
        return False
        
    try:
        embeds = []
        for item in results:
            embed = {
                "title": item['title'],
                "description": f"{item['summary']}\n\n[קרא עוד]({item['link']})",
                "url": item['link'],
                "color": 3447003,
                "timestamp": datetime.utcnow().isoformat()
            }
            if item.get('image'):
                embed["image"] = {"url": item['image']}
            embeds.append(embed)

        payload = {
            "username": "Ynet Tech Briefing",
            "embeds": embeds[:10] # Discord allows up to 10 embeds per message
        }
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        return True
    except Exception as e:
        logging.error(f'Failed to send discord notification: {e}')
        return False
