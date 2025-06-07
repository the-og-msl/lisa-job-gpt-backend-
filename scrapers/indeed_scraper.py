from datetime import date


def fetch_jobs():
    return [
        {
            "title": "Strategic Investment Manager",
            "company": "UK Infrastructure Bank",
            "location": "London",
            "description": "Leads strategic finance initiatives...",
            "red_flags": "UK nationals only",
            "link": "https://example.com/job-1",
            "posted_date": str(date.today())
        },
        {
            "title": "ESG Audit Officer",
            "company": "Generic Bank",
            "location": "Remote",
            "description": "Internal audit responsibilities...",
            "red_flags": "ACA required",
            "link": "https://example.com/job-2",
            "posted_date": str(date.today())
        }
    ]
