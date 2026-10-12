import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def answer_question(article, question):

    prompt = f"""
You are an intelligent news assistant.

Read the following news article carefully.

News Article:
{article}

Question:
{question}

Answer the question only from the given article.
If the answer is not available, reply:
"Information not available in the article."
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text