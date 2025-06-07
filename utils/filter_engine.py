import json


def load_preferences(path="preferences.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def filter_jobs(jobs, preferences):
    filtered = []
    for job in jobs:
        title = job["title"].lower()
        org = job["company"].lower()
        description = job["description"].lower()
        red_flags = job.get("red_flags", "").lower()

        if any(term.lower() in title for term in preferences["exclusion_terms"]["title"]):
            continue
        if any(term.lower() in org for term in preferences["exclusion_terms"]["organization"]):
            continue
        if any(term.lower() in red_flags for term in preferences["exclusion_terms"]["red_flags"]):
            continue
        if preferences["location"].lower() not in job["location"].lower():
            continue

        filtered.append(job)

    return filtered
