import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import spacy
import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Ensure you have downloaded the necessary NLTK data files
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt_tab')

# Load the spaCy model for NER
nlp = spacy.load('en_core_web_sm')

def preprocess_legal_text(text):
    # Initialize stop words and lemmatizer
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
    # Tokenize and remove stop words
    words = nltk.word_tokenize(text)
    words = [word for word in words if word.lower() not in stop_words]
    
    # Lemmatize words
    lemmatized_text = ' '.join([lemmatizer.lemmatize(word) for word in words])
    
    # Perform Named Entity Recognition using spaCy
    doc = nlp(lemmatized_text)
    entities = {
        'case_numbers': [],
        'statutes': [],
        'citations': [],
        'others': []
    }
    
    for ent in doc.ents:
        if ent.label_ == 'LAW':
            entities['statutes'].append(ent.text)
        elif ent.label_ == 'CARDINAL':
            entities['case_numbers'].append(ent.text)
        elif ent.label_ == 'DATE':
            entities['citations'].append(ent.text)
        else:
            entities['others'].append((ent.text, ent.label_))
    
    # Return the processed text and identified entities
    return lemmatized_text, entities

# Example usage
pdf_text = extract_text_from_pdf('sample.pdf')
cleaned_text, identified_entities = preprocess_legal_text(pdf_text)

print("Cleaned Text:")
print(cleaned_text)
print("\nIdentified Entities:")
print(identified_entities)
