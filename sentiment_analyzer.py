# %%
from textblob import TextBlob
import spacy

# %%
nlp = spacy.load('en_core_web_sm')

# %%
def analyze_entity_sentiment(text, entity_dict):
    doc = nlp(text)
    sentences = list(doc.sents)
    sentiment_map = {}

    for label, entities in entity_dict.items():
        for entity in entities:
            sentiment_scores = []
            for sent in sentences:
                if entity in sent.text:
                    blob = TextBlob(sent.text)
                    sentiment_scores.append(blob.sentiment.polarity)
            if sentiment_scores:
                avg_sentiment = round(sum(sentiment_scores) / len(sentiment_scores), 3)
                sentiment_map[entity] = avg_sentiment
            else:
                sentiment_map[entity] = None
    
    return sentiment_map

# %%



