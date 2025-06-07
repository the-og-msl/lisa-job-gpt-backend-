# Lisa Job GPT Backend

This repository contains a minimal FastAPI app that demonstrates how a custom GPT could filter and surface job listings.

## Step-by-Step Local Setup

1. **Install dependencies**
   ```bash
   pip install fastapi uvicorn
   ```
   Or install using the provided `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```
2. **Project structure**

   ```text
   lisa-job-gpt-backend/
   ├── main.py               <- FastAPI app
   ├── scrapers/
   │   └── indeed_scraper.py <- Scraping script example
   ├── utils/
   │   └── filter_engine.py  <- Filtering logic
   ├── preferences.json      <- Job preferences
   └── requirements.txt
   ```

3. **Run the API locally**
   ```bash
   uvicorn main:app --reload
   ```
   Open your browser at <http://127.0.0.1:8000/docs> to access the interactive docs.

## Overview

- **preferences.json** stores locations, red flags and other filtering options.
- **filter_engine.py** loads the preferences and applies them to job listings.
- **indeed_scraper.py** is a placeholder showing how you could fetch jobs from Indeed or another job board.
- **main.py** exposes a single endpoint to demonstrate the job scanning API.

This project is intentionally simple so you can extend it with your own scraping and filtering logic.
