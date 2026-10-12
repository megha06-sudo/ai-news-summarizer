import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):

    doc = nlp(text)

    cleaned_words = []

    for token in doc:

        if not token.is_stop and not token.is_punct:
            cleaned_words.append(token.lemma_.lower())

    return " ".join(cleaned_words)