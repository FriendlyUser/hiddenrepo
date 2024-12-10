import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import spacy
import re
from typing import Dict, List, Tuple
import logging

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

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

class LegalTextPreprocessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        # Add custom legal stop words
        self.legal_stop_words = {'court', 'case', 'law', 'section', 'pursuant'}
        self.stop_words.update(self.legal_stop_words)
        
        # Compile regex patterns for legal entities
        self.patterns = {
            'case_numbers': r'\d{2}-\d{4}|\d{1,2}:\d{2}-[a-zA-Z]{2}-\d{1,5}',
            'citations': r'\d+\s+U\.S\.\s+\d+|\d+\s+S\.Ct\.\s+\d+',
            'statutes': r'§\s*\d+(\.\d+)*|\d+\s+U\.S\.C\.\s+§\s*\d+',
        }
        
    def clean_text(self, text: str) -> str:
        """Basic text cleaning."""
        try:
            # Remove extra whitespace
            text = re.sub(r'\s+', ' ', text)
            # Remove special characters but keep legal symbols
            text = re.sub(r'[^\w\s§.]', ' ', text)
            return text.strip()
        except Exception as e:
            logging.error(f"Error in clean_text: {str(e)}")
            return text

    def lemmatize_text(self, text: str) -> str:
        """Lemmatize text while preserving legal terms."""
        try:
            tokens = word_tokenize(text)
            # Preserve certain legal terms
            legal_terms = {'habeas corpus', 'de facto', 'prima facie'}
            
            lemmatized_tokens = []
            for token in tokens:
                if token.lower() in legal_terms:
                    lemmatized_tokens.append(token)
                else:
                    lemmatized_tokens.append(self.lemmatizer.lemmatize(token))
            
            return ' '.join(lemmatized_tokens)
        except Exception as e:
            logging.error(f"Error in lemmatize_text: {str(e)}")
            return text

    def extract_legal_entities(self, text: str) -> Dict[str, List[str]]:
        """Extract legal entities using spaCy and regex patterns."""
        entities = {
            'case_numbers': [],
            'citations': [],
            'statutes': [],
            'organizations': [],
            'persons': [],
            'dates': []
        }
        
        try:
            # Regex-based extraction
            for entity_type, pattern in self.patterns.items():
                matches = re.finditer(pattern, text)
                entities[entity_type].extend([m.group() for m in matches])

            # spaCy NER
            doc = nlp(text)
            for ent in doc.ents:
                if ent.label_ == 'ORG':
                    entities['organizations'].append(ent.text)
                elif ent.label_ == 'PERSON':
                    entities['persons'].append(ent.text)
                elif ent.label_ == 'DATE':
                    entities['dates'].append(ent.text)

            # Remove duplicates and sort
            for key in entities:
                entities[key] = sorted(list(set(entities[key])))
                
            return entities
        except Exception as e:
            logging.error(f"Error in extract_legal_entities: {str(e)}")
            return entities

    def preprocess_legal_text(self, text: str) -> Tuple[str, Dict[str, List[str]]]:
        """Main preprocessing function."""
        try:
            # Initialize logging
            logging.basicConfig(level=logging.INFO)
            
            # Step 1: Clean text
            cleaned_text = self.clean_text(text)
            
            # Step 2: Lemmatize
            lemmatized_text = self.lemmatize_text(cleaned_text)
            
            # Step 3: Remove stop words
            tokens = word_tokenize(lemmatized_text)
            filtered_tokens = [token for token in tokens 
                             if token.lower() not in self.stop_words]
            processed_text = ' '.join(filtered_tokens)
            
            # Step 4: Extract entities
            entities = self.extract_legal_entities(text)  # Use original text for entity extraction
            
            return processed_text, entities
            
        except Exception as e:
            logging.error(f"Error in preprocess_legal_text: {str(e)}")
            return text, {}

# Example usage
def process_legal_document(pdf_path: str) -> Tuple[str, Dict[str, List[str]]]:
    """Process a legal document from PDF."""
    try:
        # Extract text from PDF
        raw_text = extract_text_from_pdf(pdf_path)
        
        # Initialize preprocessor
        preprocessor = LegalTextPreprocessor()
        
        # Process text
        processed_text, entities = preprocessor.preprocess_legal_text(raw_text)
        
        return processed_text, entities
        
    except Exception as e:
        logging.error(f"Error processing document: {str(e)}")
        return "", {}


pdf_path = "sample.pdf"
processed_text, entities = process_legal_document(pdf_path)

# Print results
print("Processed Text:", processed_text[:200])  # First 200 characters
print("\nExtracted Entities:")
for entity_type, entity_list in entities.items():
    print(f"{entity_type}: {entity_list}")