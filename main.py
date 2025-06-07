from fastapi import FastAPI, Query
from scrapers.indeed_scraper import fetch_jobs
from utils.filter_engine import filter_jobs, load_preferences
from pydantic import BaseModel
from typing import List

app = FastAPI()



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
    """Return recent public policy jobs scraped from Indeed."""
    return fetch_jobs(location)

<<<< codex/define-root-endpoint

@app.get("/")
def root():
    return {"message": "Lisa Job GPT Backend is live 🚀"}
====
# Add a root endpoint to fix the Render 404
@app.get("/")
def root():
    """Health check route for Render."""
    return {"message": "Lisa GPT Backend is live!"}


@app.get("/jobs")
def get_filtered_jobs(location: str = None):
    """Return job listings filtered by user preferences."""
    preferences = load_preferences()
    if location:
        preferences["location"] = location
    jobs = fetch_jobs()
    return filter_jobs(jobs, preferences)
>>> main
