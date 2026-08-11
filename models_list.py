import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)


def detect_fake_news(news):

    prompt = f"""
You are an AI Fake News Detector.

Your job is to determine whether the given news is likely REAL or FAKE.

News:
{news}

Rules:
1. Reply ONLY with YES or NO.
2. YES = The news appears to be REAL.
3. NO = The news appears to be FAKE.
4. Do not explain.
5. Do not write anything except YES or NO.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        answer = response.text.strip().upper()

        if "YES" in answer:
            return "YES"

        elif "NO" in answer:
            return "NO"

        else:
            return "UNKNOWN"

    except Exception as e:
        return f"ERROR: {e}"