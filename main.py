from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
import datetime
import requests
from bs4 import BeautifulSoup

app = FastAPI(
    title="Lisa's Strategic Job Scanner",
    description="Filters public sector and multilateral roles based on Lisa Mouslech’s career direction.",
    version="1.0.0",
    servers=[{
        "url": "https://lisa-job-gpt-backend.onrender.com",
        "description": "Live Render server"
    }]
)


@app.get("/")
def root():
    return {"message": "Lisa Job GPT Backend is live 🚀"}

class Job(BaseModel):
    title: str
    company: str
    location: str
    description: str
    requirements: List[str]
    skills: List[str]
    fit_score: int
    why_fit: str
    red_flags: str
    link: str
    salary_range: str
    posted_date: str


def fetch_jobs(location: str = "London") -> List[Job]:
    """Scrape public policy jobs from Indeed for the given location."""
    url = f"https://uk.indeed.com/jobs?q=public+policy&l={location}"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")

    jobs = []
    for card in soup.select(".job_seen_beacon")[:10]:
        try:
            title = card.select_one("h2.jobTitle").get_text(strip=True)
            company = card.select_one(".companyName").get_text(strip=True)
            link = "https://uk.indeed.com" + card.select_one("a")["href"]

            jobs.append(
                Job(
                    title=title,
                    company=company,
                    location=location,
                    description="",
                    requirements=[],
                    skills=[],
                    fit_score=0,
                    why_fit="",
                    red_flags="",
                    link=link,
                    salary_range="",
                    posted_date=str(datetime.date.today()),
                )
            )
        except Exception:
            continue
    return jobs

@app.get("/scan-roles/", response_model=List[Job])
def scan_roles(location: str = Query("London")):
    """Return recent public policy jobs scraped from Indeed."""
    return fetch_jobs(location)
