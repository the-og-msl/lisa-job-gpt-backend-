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
    limit: int = Query(
        default=15,
        description="Maximum number of results to return",
    ),
    offset: int = Query(
        default=0,
        description="Number of results to skip before returning data",
    ),
):
    """Return job listings from either JobSpy or the Civil Service site.

    Parameters
    ----------
    keyword: str
        Search keyword to filter results.
    location: str
        City or region to search within.
    source: str
        Data source to use, either ``jobspy`` or ``civil_service``.
    limit: int
        Maximum number of results to return (default ``15``).
    offset: int
        Number of results to skip before starting the slice (default ``0``).
    """
    if source == "jobspy":
        return fetch_jobspy_jobs(keyword=keyword, location=location)

    try:
        jobs = fetch_civil_service_jobs(keyword=keyword, location=location)
    except Exception:
        jobs = fetch_fallback_jobs(keyword=keyword, location=location)

    return jobs[offset: offset + limit]
