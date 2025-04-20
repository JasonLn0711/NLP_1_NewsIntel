# %%
import spacy

nlp = spacy.load('en_core_web_sm')

# %%
def extract_entities(text):
    doc = nlp(text)
    entity_dict = {}

    for ent in doc.ents:
        if ent.label_ not in entity_dict:
            entity_dict[ent.label_] = set()
        entity_dict[ent.label_].add(ent.text)

    # Convert sets to lists for JSON compatibility or further use
    return {label: list(ents) for label, ents in entity_dict.items()}


