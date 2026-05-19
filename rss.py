import feedparser
import time
from datetime import datetime, timedelta
import logging

def get_recent_articles(feeds, hours=48):
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
                
                # Check for publication date
                pub_dt = None
                published = getattr(entry, 'published_parsed', None)
                if published:
                    pub_dt = datetime.fromtimestamp(time.mktime(published))
                elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                    pub_dt = datetime.fromtimestamp(time.mktime(entry.updated_parsed))
                
                # If we have a date, filter by cutoff. If not, include anyway to be safe.
                if pub_dt and pub_dt < cutoff:
                    continue

                # Trim summary heavily to save tokens
                summary_text = getattr(entry, 'summary', '')
                clean_summary = summary_text[:300] 
                
                articles.append({
                    'title': title,
                    'summary': clean_summary,
                    'link': entry.link
                })
                seen_titles.add(title.lower())
        except Exception as e:
            logging.error(f'Error fetching {url}: {e}')
            
    return articles
