import yake

kw_extractor = yake.KeywordExtractor(
    lan="en",
    n=1,
    top=10
)

def extract_keywords(text):

    keywords = kw_extractor.extract_keywords(text)

    return [keyword for keyword, score in keywords]