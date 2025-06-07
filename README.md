# Lisa Job GPT Backend

This repository provides a small FastAPI service that exposes an API endpoint for scanning
job listings. Listings are filtered using criteria stored in `preferences.json`.

## Project Structure
```
lisa-job-gpt-backend/
├── main.py                 # FastAPI application
├── scrapers/
│   └── indeed_scraper.py   # Example scraper returning sample jobs
├── utils/
│   └── filter_engine.py    # Filtering logic
├── preferences.json        # Example preferences
├── requirements.txt
```

## Getting Started
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the API locally:
   ```bash
   uvicorn main:app --reload
   ```
3. Visit `http://127.0.0.1:8000/docs` for interactive documentation.

The API loads `preferences.json` and filters scraped jobs based on exclusion
terms and location. Modify the JSON file to suit your needs.
