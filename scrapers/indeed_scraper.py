from datetime import date


def fetch_jobs():
    return [
        {
            "title": "Policy Analyst",
            "organization": "Department of Energy",
            "description": "Climate strategy and green finance...",
            "location": "london",
            "red_flags": "",
            "link": "https://example.com/job1",
            "posted_date": str(date.today())
        },
        {
            "title": "Senior Analyst",
            "organization": "UK Finance",
            "description": "Public sector finance, ESG policy...",
            "location": "remote",
            "red_flags": "requires UK gov clearance",
            "link": "https://example.com/job2",
            "posted_date": str(date.today())
        }
    ]
