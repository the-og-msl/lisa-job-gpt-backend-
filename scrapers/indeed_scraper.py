import feedparser


def fetch_jobs(keyword: str | None = None, location: str | None = None):
    """Fetch job listings from the Civil Service RSS feed.

    Both ``keyword`` and ``location`` are optional and are used to filter
    the returned entries if provided.
    """
    url = (
        "https://www.civilservicejobs.service.gov.uk/rss/civilservice/alljobs.rss"
    )
    feed = feedparser.parse(url)

    jobs = []
    for entry in feed.entries:
        title = entry.title
        summary = entry.get("summary", "")

        if keyword and keyword.lower() not in title.lower() and keyword.lower() not in summary.lower():
            continue
        if location and location.lower() not in title.lower():
            continue

        jobs.append(
            {
                "title": title,
                "link": entry.link,
                "published": entry.published,
                "summary": summary,
            }
        )
    return jobs
