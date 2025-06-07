import json
from typing import List, Dict, Any

PREFERENCES_PATH = "preferences.json"


def load_preferences(path: str = PREFERENCES_PATH) -> Dict[str, Any]:
    """Load user job preferences from a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def filter_jobs(
    jobs: List[Dict[str, Any]],
    preferences: Dict[str, Any],
) -> List[Dict[str, Any]]:
    """Filter a list of jobs using preference rules."""
    filtered: List[Dict[str, Any]] = []

    ex_terms = preferences.get("exclusion_terms", {})

    for job in jobs:
        title = job.get("title", "").lower()
        org = job.get("company", "").lower()
        red_flags = job.get("red_flags", "").lower()
        location = job.get("location", "").lower()

        if any(term.lower() in title for term in ex_terms.get("title", [])):
            continue
        if any(
            term.lower() in org
            for term in ex_terms.get("organization", [])
        ):
            continue
        if any(
            term.lower() in red_flags
            for term in ex_terms.get("red_flags", [])
        ):
            continue
        if (
            preferences.get("location")
            and preferences["location"].lower() not in location
        ):
            continue

        filtered.append(job)

    return filtered
