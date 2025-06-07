from typing import List, Dict


def scrape_jobs() -> List[Dict]:
    """Return example job postings. In production, implement real scraping."""
    return [
        {
            "title": "Senior Policy Advisor",
            "company": "HM Treasury",
            "location": "London",
            "description": "Lead economic strategy workstreams with ministers.",
            "requirements": ["Masters in Economics", "5+ years in policy"],
            "skills": ["Policy Analysis", "Stakeholder Management"],
            "fit_score": 0,
            "why_fit": "",
            "red_flags": "May require UK gov reference.",
            "link": "https://example.com/hmt-senior-policy-advisor",
            "salary_range": "£65,000–£85,000",
            "posted_date": "2024-01-01",
        },
        {
            "title": "Policy Intern",
            "company": "BadCompany",
            "location": "London",
            "description": "Assist with policy drafting.",
            "requirements": ["Bachelor's"],
            "skills": ["Writing"],
            "fit_score": 0,
            "why_fit": "",
            "red_flags": "unpaid position",
            "link": "https://example.com/policy-intern",
            "salary_range": "N/A",
            "posted_date": "2024-01-02",
        },
    ]
