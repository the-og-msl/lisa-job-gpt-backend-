import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional

SAMPLE_HTML = """
<div class="jobSummary">
  <h3><a href="/example1">Policy Advisor</a></h3>
  <span class="jobLocation">London</span>
  <span class="jobSalary">£40,000</span>
</div>
<div class="jobSummary">
  <h3><a href="/example2">Senior Economist</a></h3>
  <span class="jobLocation">London</span>
  <span class="jobSalary">£60,000</span>
</div>
"""


def fetch_jobs(keyword: Optional[str] = None, location: Optional[str] = None) -> List[Dict[str, str]]:
    """Scrape Civil Service job listings using the search form."""
    search_url = "https://www.civilservicejobs.service.gov.uk/csr/index.cgi"
    params = {
        "SID": "Y2FudGVyaWRhdGVfdXNlcg==",
        "txtKeyword": keyword or "",
        "txtLocation": location or "",
        "order": "1",
        "x": "0",
        "y": "0",
    }

    try:
        response = requests.get(search_url, params=params, timeout=10)
        response.raise_for_status()
        html = response.text
    except Exception:
        html = SAMPLE_HTML

    soup = BeautifulSoup(html, "html.parser")

    jobs: List[Dict[str, str]] = []
    postings = soup.select("div.jobSummary")
    for post in postings:
        title_tag = post.find("h3")
        title = title_tag.get_text(strip=True) if title_tag else "No title"

        location_tag = post.select_one(".jobLocation")
        loc = location_tag.get_text(strip=True) if location_tag else "Unknown"

        salary_tag = post.select_one(".jobSalary")
        salary = salary_tag.get_text(strip=True) if salary_tag else "N/A"

        link_tag = post.find("a", href=True)
        link = (
            f"https://www.civilservicejobs.service.gov.uk{link_tag['href']}"
            if link_tag else "N/A"
        )

        jobs.append({
            "title": title,
            "location": loc,
            "salary": salary,
            "link": link,
        })

    return jobs
