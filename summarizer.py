# %%
import spacy
from collections import Counter

# %%
nlp = spacy.load('en_core_web_sm')

# %%
def extract_keywords(text, top_n=10):
    doc = nlp(text.lower())
    keywords = [
        token.lemma_ 
        for token in doc 
        if token.is_alpha 
        and not token.is_stop 
        and token.pos_ in ["NOUN", "PROPN", "VERB"]]
    return [word for word, freq in Counter(keywords).most_common(top_n)]

def build_timeline(text):
    doc = nlp(text)
    timeline = []
    for sent in doc.sents:
        sent_dates = [ent.text for ent in sent.ents if ent.label_ == "DATE"]
        if sent_dates:
            event_verb = next(
                (token.lemma_ for token in sent if token.pos_ == "VERB"),
                None)
            timeline.append({
                "date": sent_dates[0],
                "event_summary": sent.text.strip(),
                "main_action": event_verb
            })
    
    return timeline

# %%



