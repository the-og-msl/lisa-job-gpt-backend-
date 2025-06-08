import json


def load_preferences(path="preferences.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def filter_jobs(jobs, preferences):
    """Filter job listings based on simple preference criteria."""
    filtered = []
    for job in jobs:
        title = job["title"].lower()
        org = job.get("organization", job.get("company", "")).lower()
        description = job.get("description", "").lower()
        red_flags = job.get("red_flags", "").lower()

        # Include jobs that match any preferred keywords in the title or description
        keywords = [k.lower() for k in preferences.get("keywords", [])]
        if keywords and not any(k in title or k in description for k in keywords):
            continue

        # Skip jobs that do not match the preferred location
        if "location" in preferences and preferences["location"].lower() not in job["location"].lower():
            continue

        filtered.append(job)

    return filtered
