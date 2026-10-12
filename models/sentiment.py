import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def analyze_sentiment(article):

    prompt = f"""
Analyze the sentiment of the following news article.

Return ONLY one of these:

Positive
Negative
Neutral

News:
{article}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()