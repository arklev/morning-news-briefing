import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
NTFY_URL = os.getenv('NTFY_URL')
NTFY_USER = os.getenv('NTFY_USER')
NTFY_PASS = os.getenv('NTFY_PASS')

RSS_FEEDS = [
    'https://www.ynet.co.il/Integration/StoryRss2.xml',    # News
    'https://www.ynet.co.il/Integration/StoryRss6.xml',    # Economy
    'https://www.ynet.co.il/Integration/StoryRss544.xml',  # Tech
    'https://www.artificialintelligence-news.com/feed/'   # AI News (English)
]

LOG_FILE = 'morning_briefing.log'
