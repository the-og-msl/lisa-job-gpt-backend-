# Lisa Job GPT Backend

This FastAPI application exposes an endpoint for scanning public policy roles. It scrapes the UK Civil Service jobs site for the latest postings.

## Running locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open `http://localhost:8000/docs` for the interactive API docs.

Set the `CIVIL_SERVICE_SID` environment variable with the encoded SID from the
Civil Service Jobs website if you need to override the default. The application
falls back to `YXBpX3NlYXJjaF9mb3Jt` when the variable is not provided.

The `/jobs` endpoint accepts optional `keyword` and `location` query parameters and defaults to `policy` and `london` if omitted. Pagination is supported using `limit` and `offset` parameters which default to `15` and `0` respectively.
