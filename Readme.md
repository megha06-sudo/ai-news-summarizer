# Intelligent News Summarization and Sentiment Analysis System

## Project Description

This project is a Flask-based web application that uses Natural Language Processing (NLP) and Google's Gemini Large Language Model (LLM) to analyze news articles.

The system can:

- Summarize lengthy news articles
- Detect sentiment
- Extract important keywords
- Identify named entities
- Answer user questions related to the article
- Analyze news directly from a URL

---

## Technologies Used

- Python
- Flask
- Google Gemini API
- spaCy
- YAKE
- Newspaper3k
- Bootstrap 5
- HTML
- CSS
- JavaScript

---



---

## Installation

### Step 1

Clone or download the project.

### Step 2

Create a virtual environment.

```
python -m venv venv
```

### Step 3

Activate the virtual environment.

Windows:

```
venv\Scripts\activate
```

### Step 4

Install the required libraries.

```
pip install -r requirements.txt
```

### Step 5

Download the spaCy model.

```
python -m spacy download en_core_web_sm
```

### Step 6

Create a file named `.env`

Add your Gemini API Key.

```
GEMINI_API_KEY=YOUR_API_KEY
```

### Step 7

Run the application.

```
python app.py
```

Open the browser:

```
http://127.0.0.1:5000
```

---


