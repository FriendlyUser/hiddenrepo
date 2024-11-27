import spacy
from transformers import pipeline
def process_user_message(message):



    nlp = spacy.load('en_core_web_sm')
    classifier = pipeline('sentiment-analysis')

    if not isinstance(message, str):
        raise ValueError("""Input must be a string.""")


    doc = nlp(message)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    sentiment = classifier(message)[0]


    return {
        'entities': entities,
        'sentiment': sentiment
    }