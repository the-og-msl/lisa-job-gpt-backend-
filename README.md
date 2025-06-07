# Lisa Job GPT Backend

This FastAPI application exposes an endpoint for scanning public policy roles. It scrapes Indeed for the latest postings in a given location.

## Running locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open `http://localhost:8000/docs` for the interactive API docs.
