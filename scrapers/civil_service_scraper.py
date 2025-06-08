import requests
from bs4 import BeautifulSoup
from datetime import date

def fetch_jobs(keyword="policy", location="london"):
    url = "https://www.civilservicejobs.service.gov.uk/csr/index.cgi"
    params = {
        "SID": "YXBpX3NlYXJjaF9mb3Jt",
        "jcode": "",
        "txtSearch": keyword,
        "postcode": location,
        "radius": "10",
        "submit1": "Search"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (JobScannerBot)"
    }

    response = requests.get(url, params=params, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    for row in soup.select("div.results div.job"):
        title_elem = row.select_one("h3 a")
        org_elem = row.select_one("div.org")
        loc_elem = row.select_one("div.location")
        summary_elem = row.select_one("div.summary")

        job_url = "https://www.civilservicejobs.service.gov.uk" + title_elem.get("href")

        results.append({
            "title": title_elem.text.strip() if title_elem else "N/A",
            "organization": org_elem.text.strip() if org_elem else "N/A",
            "location": loc_elem.text.strip() if loc_elem else "N/A",
            "description": summary_elem.text.strip() if summary_elem else "N/A",
            "red_flags": "",
            "link": job_url,
            "posted_date": str(date.today())
        })

    return results
