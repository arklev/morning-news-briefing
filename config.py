import os
from dotenv import load_dotenv

load_dotenv()

# Use absolute paths for reliability
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Notification Settings
NOTIFICATION_CHANNEL = os.getenv('NOTIFICATION_CHANNEL', 'ntfy')
NTFY_URL = os.getenv('NTFY_URL')
NTFY_USER = os.getenv('NTFY_USER')
NTFY_PASS = os.getenv('NTFY_PASS')
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

RSS_FEEDS = [
    'https://www.ynet.co.il/Integration/StoryRss544.xml'
]

LOG_FILE = os.path.join(BASE_DIR, 'morning_briefing.log')
