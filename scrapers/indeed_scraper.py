# Placeholder Indeed scraper

from typing import List, Dict


def fetch_jobs(query: str, location: str) -> List[Dict]:
    """Return mock jobs for the given query and location."""
    return [
        {
            "title": "Example Job",
            "company": "Example Corp",
            "location": location,
            "description": "Sample description",
            "link": "https://example.com/job",
        }
    ]
