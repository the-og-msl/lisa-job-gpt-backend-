# Lisa Job GPT Backend

This FastAPI application exposes an endpoint for scanning public policy roles. It scrapes the Civil Service Jobs site for the latest postings in a given location.

## Running locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open `http://localhost:8000/docs` for the interactive API docs.

### Environment variables

Set `CIVIL_SERVICE_SID` to the SID value from a working Civil Service Jobs
search URL. Without this value the scraper may return no results.
