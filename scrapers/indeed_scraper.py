"""Simple scraper for the Civil Service jobs board."""

from datetime import date
from typing import List, Dict

import requests
from bs4 import BeautifulSoup


def fetch_jobs() -> List[Dict[str, str]]:
    """Scrape the first page of Civil Service job listings."""

    url = "https://www.civilservicejobs.service.gov.uk/csr/index.cgi"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for job_row in soup.select(".searchResult .job"):
        title_elem = job_row.select_one("h3")
        link_elem = job_row.select_one("a")
        if not title_elem or not link_elem:
            continue

        title = title_elem.get_text(strip=True)
        link = link_elem["href"]

        jobs.append(
            {
                "title": title,
                "company": "Civil Service",
                "location": "",
                "description": "",
                "red_flags": "",
                "link": f"https://www.civilservicejobs.service.gov.uk{link}",
                "posted_date": str(date.today()),
            }
        )

    return jobs
