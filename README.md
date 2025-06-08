# Lisa Job GPT Backend

This FastAPI application exposes an endpoint for scanning public policy roles. It scrapes the UK Civil Service jobs site for the latest postings.

## Running locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open `http://localhost:8000/docs` for the interactive API docs.

The `/jobs` endpoint accepts optional `keyword` and `location` query parameters and defaults to `policy` and `london` if omitted.
