import requests
from bs4 import BeautifulSoup


def fetch_jobs():
    """Scrape Civil Service job listings (page 1 only)."""
    url = "https://www.civilservicejobs.service.gov.uk/csr/index.cgi"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    for job_row in soup.select(".searchResult .job"):
        title = job_row.select_one("h3").get_text(strip=True)
        link = job_row.select_one("a")["href"]
        jobs.append({
            "title": title,
            "link": f"https://www.civilservicejobs.service.gov.uk{link}"
        })

    return jobs
