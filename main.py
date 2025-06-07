from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List

from scrapers.indeed_scraper import scrape_jobs
from utils.filter_engine import load_preferences, filter_jobs

app = FastAPI(
    title="Lisa's Strategic Job Scanner",
    description=(
        "Filters public sector and multilateral roles based on "
        "Lisa Mouslech’s career direction."
    ),
    version="1.0.0",
    servers=[{
        "url": "https://lisa-job-gpt-backend.onrender.com",
        "description": "Live Render server"
    }]
)


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


@app.get("/scan-roles/", response_model=List[Job])
def scan_roles(location: str = Query("London")):
    """Return job listings filtered by user preferences."""
    preferences = load_preferences()

    jobs = scrape_jobs()
    # Override location if provided via query
    if location:
        preferences["location"] = location

    filtered = filter_jobs(jobs, preferences)

    return [Job(**job) for job in filtered]
