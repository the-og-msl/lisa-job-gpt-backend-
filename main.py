from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
import datetime

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
def scan_roles(location: str = Query("London")):
    today = datetime.datetime.now().date()
    return [
        Job(
            title="Senior Policy Advisor",
            company="HM Treasury",
            location="London",
            description="Develop and lead economic strategy workstreams with ministers.",
            requirements=["Masters in Economics", "5+ years in policy", "UK public sector exposure"],
            skills=["Policy Analysis", "Public Finance", "Stakeholder Management"],
            fit_score=9,
            why_fit="Direct policy impact, public-private overlap, aligns with UK gov pivot.",
            red_flags="May require UK gov reference.",
            link="https://example.com/hmt-senior-policy-advisor",
            salary_range="£65,000–£85,000",
            posted_date=str(today)
        )
    ]
