from fastapi import FastAPI
from typing import Optional

from scrapers.indeed_scraper import fetch_jobs
from utils.filter_engine import filter_jobs, load_preferences


app = FastAPI(title="Lisa's Strategic Job Scanner")


@app.get("/")
def root():
    return {"message": "Lisa Job GPT Backend is live 🚀"}


@app.get("/scan-roles")
def scan_roles(location: Optional[str] = None):
    """Return job listings filtered by user preferences."""
    preferences = load_preferences()
    jobs = fetch_jobs()

    if location:
        preferences["location"] = location.lower()

    filtered = filter_jobs(jobs, preferences)
    return filtered

