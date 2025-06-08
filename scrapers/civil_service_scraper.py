import logging
import os
from typing import List
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.civilservicejobs.service.gov.uk/csr/index.cgi"
# SID value is required for successful requests. Set via environment variable.
SID = os.getenv("CIVIL_SERVICE_SID", "someSID")


def fetch_jobs(keyword: str = "", location: str = "") -> List[dict]:
    """Scrape Civil Service Jobs listings.

    The site requires a session identifier (SID). Provide it via the
    ``CIVIL_SERVICE_SID`` environment variable.
    """
    params = {
        "SID": SID,
        "txtKeyword": keyword,
        "txtLocation": location,
        "search_page": 1,
        "order": 1,
    }

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/118.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(BASE_URL, params=params, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        logging.error("Request failed: %s", exc)
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []
    for box in soup.select("div[class*=search-results-job-box]"):
        title_link = box.select_one(".search-results-job-box-title a")
        if not title_link:
            continue

        job = {
            "title": title_link.get_text(strip=True),
            "url": urljoin(BASE_URL, title_link.get("href", "")),
            "location": "",
            "salary": "",
            "department": "",
            "closing_date": "",
            "ref_code": "",
        }

        loc_el = box.select_one(".search-results-job-box-location")
        if loc_el:
            job["location"] = loc_el.get_text(strip=True)

        sal_el = box.select_one(".search-results-job-box-salary")
        if sal_el:
            job["salary"] = sal_el.get_text(strip=True)

        dept_el = box.select_one(".search-results-job-box-department")
        if dept_el:
            job["department"] = dept_el.get_text(strip=True)

        close_el = box.select_one(".search-results-job-box-closingdate")
        if close_el:
            job["closing_date"] = close_el.get_text(strip=True)

        ref_el = box.select_one(".search-results-job-box-refcode")
        if ref_el:
            job["ref_code"] = ref_el.get_text(strip=True)

        jobs.append(job)

    if not jobs:
        logging.info("No jobs found for keyword: %s", keyword)
    return jobs
