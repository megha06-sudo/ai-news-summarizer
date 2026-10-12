import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def analyze_article(article):

    prompt = f"""
You are an AI News Analyzer.

Analyze the following news article.

Return ONLY valid JSON in this exact format.

{{
"summary":"...",
"sentiment":"Positive/Negative/Neutral"
}}

News Article:
{article}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    # Remove markdown code fences if Gemini adds them
    text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)