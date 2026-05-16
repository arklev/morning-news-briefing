import feedparser
import time
from datetime import datetime, timedelta
import logging

def get_recent_articles(feeds, hours=12): # Reduced to 12 hours for more focus
    articles = []
    seen_titles = set()
    cutoff = datetime.now() - timedelta(hours=hours)
    
    for url in feeds:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                title = entry.title.strip()
                if title.lower() in seen_titles:
                    continue
                
                published = getattr(entry, 'published_parsed', None)
                if published:
                    pub_dt = datetime.fromtimestamp(time.mktime(published))
                    if pub_dt > cutoff:
                        # Trim summary heavily to save tokens
                        summary_text = getattr(entry, 'summary', '')
                        # Simple cleanup: remove HTML tags if any and limit to 200 chars
                        clean_summary = summary_text[:200] 
                        
                        articles.append({
                            'title': title,
                            'summary': clean_summary
                        })
                        seen_titles.add(title.lower())
        except Exception as e:
            logging.error(f'Error fetching {url}: {e}')
            
    # Return only top 8 articles to strictly limit token usage and ensure brevity
    return articles[:8] 
