from fastapi import FastAPI
from scrapers.indeed_scraper import fetch_jobs

app = FastAPI()

@app.get("/")
def root():
    """Health check route for Render."""
    return {"message": "Lisa GPT Backend is live!"}

@app.get("/jobs")
def get_jobs():
    """Return job listings scraped from the Civil Service site."""
    return fetch_jobs()
