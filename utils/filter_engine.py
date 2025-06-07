"""Simple job filtering logic."""

import json
from typing import List, Dict


PREFERENCES_FILE = "preferences.json"


def load_preferences() -> Dict:
    with open(PREFERENCES_FILE, "r") as f:
        return json.load(f)


def filter_jobs(jobs: List[Dict]) -> List[Dict]:
    prefs = load_preferences()
    locations = prefs.get("locations", [])
    red_flags = set(word.lower() for word in prefs.get("red_flags", []))

    filtered = []
    for job in jobs:
        if job.get("location") not in locations:
            continue
        if any(flag in job.get("description", "").lower() for flag in red_flags):
            continue
        filtered.append(job)
    return filtered
