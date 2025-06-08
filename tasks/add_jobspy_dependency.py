# 📁 Task: Add JobSpy to requirements.txt

def run():
    with open("requirements.txt", "a") as f:
        f.write("\njobspy==0.29.0")
    print("✅ jobspy==0.29.0 appended to requirements.txt")
