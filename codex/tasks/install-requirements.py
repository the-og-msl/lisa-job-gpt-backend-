# 📁 Task: Reinstall dependencies after adding jobspy

import subprocess


def run():
    print("📦 Installing from requirements.txt...")
    result = subprocess.run(["pip", "install", "-r", "requirements.txt"], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("⚠️ Errors:", result.stderr)
