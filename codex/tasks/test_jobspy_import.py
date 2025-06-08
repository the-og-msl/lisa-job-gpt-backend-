# codex/tasks/test_jobspy_import.py

def run():
    try:
        from jobspy import scrape_jobs
        print("✅ JobSpy imported successfully.")
    except Exception as e:
        print("❌ JobSpy import failed:", e)

if __name__ == "__main__":
    run()
