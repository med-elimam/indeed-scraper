import requests
import feedparser

WEBHOOK = "PUT_YOUR_WEBHOOK_URL_HERE"

feeds = [
    "https://www.indeed.com/rss?q=embedded+systems&l=UAE",
    "https://www.indeed.com/rss?q=embedded+systems&l=Saudi+Arabia"
]

jobs = []

for url in feeds:
    feed = feedparser.parse(url)
    for entry in feed.entries:
        jobs.append({
            "job_title": entry.title,
            "company_name": entry.get("author", "Unknown"),
            "job_url": entry.link,
            "country": "UAE" if "UAE" in url else "KSA",
            "source_platform": "indeed",
            "raw_description": entry.summary
        })

if jobs:
    requests.post(WEBHOOK, json=jobs)
