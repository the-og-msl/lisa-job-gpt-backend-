from fastapi import FastAPI, Query
from scrapers.civil_service_scraper import fetch_jobs as fetch_civil_service_jobs
from scrapers.indeed_scraper import fetch_jobs as fetch_fallback_jobs
from scrapers.jobspy_scraper import fetch_jobs as fetch_jobspy_jobs

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
def get_jobs(
    keyword: str = Query(
        default="policy",
        description="Search keyword (e.g. 'policy', 'economics', 'finance')",
    ),
    location: str = Query(
        default="london",
        description="Location to filter by (e.g. 'London')",
    ),
    source: str = Query(
        default="jobspy",
        description="Data source ('jobspy' or 'civil_service')",
    ),
):
    """Return job listings from either JobSpy or the Civil Service site."""
    if source == "jobspy":
        return fetch_jobspy_jobs(keyword=keyword, location=location)

    try:
        return fetch_civil_service_jobs(keyword=keyword, location=location)
    except Exception:
        return fetch_fallback_jobs(keyword=keyword, location=location)
