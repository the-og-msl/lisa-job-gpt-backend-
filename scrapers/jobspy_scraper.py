from jobspy import scrape_jobs
from datetime import date


def fetch_jobs(keyword="policy", location="London"):
    jobs = scrape_jobs(
        site_name=["indeed", "linkedin", "glassdoor"],
        search_term=keyword,
        location=location,
        results_wanted=20,
        hours_old=336,  # past 14 days
        country_indeed="UK",
    )

    jobs = jobs.fillna("")  # Fill empty fields

    results = []

    for _, row in jobs.iterrows():
        results.append(
            {
                "title": row["title"],
                "organization": row["company_name"],
                "location": row["location"],
                "description": row["description"],
                "red_flags": "",
                "link": row["job_url"],
                "posted_date": str(date.today()),
            }
        )

    return results
