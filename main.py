from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Dict
import datetime

from scrapers.indeed_scraper import fetch_jobs
from utils.filter_engine import filter_jobs

app = FastAPI(
    title="Lisa's Strategic Job Scanner",
    description="Filters public sector and multilateral roles based on Lisa Mouslech’s career direction.",
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
def scan_roles(query: str = Query("policy"), location: str = Query("London")):
    """Return filtered jobs for the given query and location."""
    jobs: List[Dict] = fetch_jobs(query, location)
    filtered = filter_jobs(jobs)

    today = datetime.datetime.now().date()
    results: List[Job] = []
    for job in filtered:
        results.append(
            Job(
                title=job.get("title", ""),
                company=job.get("company", ""),
                location=job.get("location", ""),
                description=job.get("description", ""),
                requirements=job.get("requirements", []),
                skills=job.get("skills", []),
                fit_score=10,
                why_fit="",  # In a real app calculate the reason
                red_flags="",  # In a real app expose any issues
                link=job.get("link", ""),
                salary_range=job.get("salary_range", ""),
                posted_date=str(today),
            )
        )
    return results
