import json


def load_preferences(path="preferences.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def filter_jobs(jobs, preferences):
    filtered = []
    red_flags = preferences["exclusion_terms"]["red_flags"]
    for job in jobs:
        title = job["title"].lower()
        org = job["organization"].lower()
        red_flag_text = job.get("red_flags", "").lower()

        if any(term in title for term in preferences["exclusion_terms"]["title"]):
            continue
        if any(term in org for term in preferences["exclusion_terms"]["organization"]):
            continue
        if any(term in red_flag_text for term in red_flags):
            continue
        if preferences["location"] not in job["location"].lower():
            continue

        filtered.append(job)

    return filtered
