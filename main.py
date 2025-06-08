from fastapi import FastAPI
from scrapers.civil_service_scraper import fetch_jobs

app = FastAPI(
    title="Lisa's Strategic Job Scanner",
    description="Filters public sector and multilateral roles based on Lisa Mouslech's career direction.",
    version="1.0.0",
    servers=[
        {
            "url": "https://lisa-job-gpt-backend.onrender.com",
            "description": "Render deployment"
        }
    ]
)


@app.get("/")
def root():
    """Health check route for Render."""
    return {"message": "Lisa GPT Backend is live!"}


@app.get("/jobs")
def get_jobs(keyword: str = "", location: str = ""):
    """Return job listings scraped from the Civil Service site."""
    return fetch_jobs(keyword=keyword, location=location)
