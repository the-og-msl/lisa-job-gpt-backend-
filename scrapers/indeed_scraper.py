import feedparser


def fetch_jobs(location: str = None):
    """Fetch job listings from the Civil Service RSS feed.
    Optionally filters by keyword if `location` is provided.
    """
    url = (
        "https://www.civilservicejobs.service.gov.uk/rss/civilservice/alljobs.rss"
    )
    feed = feedparser.parse(url)

    jobs = []
    for entry in feed.entries:
        if location and location.lower() not in entry.title.lower():
            continue
        jobs.append(
            {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published,
                "summary": entry.get("summary", ""),
            }
        )
    return jobs
