
from models.article_extractor import extract_article
import os
from models.qa import answer_question
from models.preprocess import preprocess_text
from models.keyword import extract_keywords
from models.ner import extract_entities
from models.sentiment import analyze_sentiment
from flask import Flask, render_template, request
from models.summarizer import generate_summary
from models.analyzer import analyze_article

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    try:

        article = request.form.get("article", "").strip()
        url = request.form.get("url", "").strip()
        if not article and url:
            article = extract_article(url)
        if not article:

            return render_template(
                "index.html",
                error="Please paste an article or enter a news URL."
            )

        cleaned_text = preprocess_text(article)

        analysis = analyze_article(article)
        summary = analysis["summary"]

        sentiment = analysis["sentiment"]

        keywords = extract_keywords(cleaned_text)

        entities = extract_entities(article)

        return render_template(
            "result.html",
            article=article,
            summary=summary,
            sentiment=sentiment,
            keywords=keywords,
            entities=entities,
            answer=None
        )

    except Exception as e:

        return render_template(
            "index.html",
            error="Unable to analyze the article at the moment. Please check your internet connection or try again later."
        )  
@app.route("/ask", methods=["POST"])
def ask():

    try:

        article = request.form["article"]

        summary = request.form["summary"]

        sentiment = request.form["sentiment"]

        question = request.form["question"]

        keywords = extract_keywords(preprocess_text(article))

        entities = extract_entities(article)

        answer = answer_question(article, question)

        return render_template(
            "result.html",
            article=article,
            summary=summary,
            sentiment=sentiment,
            keywords=keywords,
            entities=entities,
            answer=answer
        )

    except Exception as e:
        answer = "Unable to answer your question right now. Please try again."

        return render_template(
            "result.html",
            article=article,
            summary=summary,
            sentiment=sentiment,
            keywords=keywords,
            entities=entities,
            answer=answer
        )

if __name__ == "__main__":
    app.run(debug=True)