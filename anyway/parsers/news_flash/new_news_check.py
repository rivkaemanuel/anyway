from datetime import datetime
import feedparser

from .news_flash_parser import get_latest_date_from_db


def is_new_flash_news(rss_link):
    d = feedparser.parse(rss_link)
    latest_date = get_latest_date_from_db()
    newest_entry = datetime.strptime(d.entries[0].published[:-6], '%a, %d %b %Y %H:%M:%S')
    newest_entry = newest_entry.replace(tzinfo=None)
    if latest_date is None:
        return True
    return newest_entry > latest_date
