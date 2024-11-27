"
 I m tweaking this function that processes user inputs for our AI chatbot using spaCy and HuggingFace Transformers. I want to make sure it's solid and handles all the weird edge cases.Could you help me write some unit tests with pytest for it ? I need to test things like empty inputs, non-text data, different languages, maybe some special characters.Here's the function:
 

 def process_user_message(message):
  import spacy
  from transformers import pipeline
 

  nlp = spacy.load('en_core_web_sm')
  classifier = pipeline('sentiment-analysis')
 

  if not isinstance(message, str):
  raise ValueError(""Input must be a string."")
 

  doc = nlp(message)
  entities = [(ent.text, ent.label_) for ent in doc.ents]
  sentiment = classifier(message)[0]
 

  return {
  'entities': entities,
  'sentiment': sentiment
  }
 

 

 I'm looking to cover as many scenarios as possible , so any help would be greate."