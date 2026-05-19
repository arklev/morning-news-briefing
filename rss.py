import feedparser
import time
from datetime import datetime, timedelta
import logging
import re

def extract_image_url(description):
    if not description:
        return None
    # Look for img src in the HTML description
    match = re.search(r'<img [^>]*src=[\'"]([^\'"]+)[\'"]', description)
    if match:
        return match.group(1)
    return None

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

                # Extract image URL from description
                image_url = extract_image_url(getattr(entry, 'description', ''))
                
                # Trim summary heavily to save tokens
                summary_text = getattr(entry, 'summary', '')
                # Remove HTML tags from summary for cleaner AI processing
                clean_summary = re.sub(r'<[^>]+>', '', summary_text)[:300] 
                
                articles.append({
                    'title': title,
                    'summary': clean_summary,
                    'link': entry.link,
                    'image': image_url
                })
                seen_titles.add(title.lower())
        except Exception as e:
            logging.error(f'Error fetching {url}: {e}')
            
    return articles
