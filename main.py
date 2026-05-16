import logging
from config import RSS_FEEDS, LOG_FILE
from rss import get_recent_articles
from summarize import summarize_news
from notify import send_notification

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run():
    logging.info("Starting Morning News Briefing...")
    
    try:
        # 1. Fetch RSS
        articles = get_recent_articles(RSS_FEEDS)
        logging.info(f"Fetched {len(articles)} recent articles.")
        
        # 2. Summarize
        summary = summarize_news(articles)
        logging.info("Summary generated.")
        
        # 3. Notify
        if send_notification(summary):
            logging.info("Notification sent successfully.")
        else:
            logging.error("Failed to send notification.")
            
    except Exception as e:
        logging.error(f"Unexpected error in main loop: {e}")

if __name__ == "__main__":
    run()
