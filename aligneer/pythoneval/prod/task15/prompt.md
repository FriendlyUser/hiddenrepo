Automated legal document analysis lately. I've crafted a function that extracts text from PDF files using PyPDF2:

import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text
Now, I need to preprocess this extracted text. The challenge is to remove stop words and perform lemmatization using NLTK, while also handling named entity recognition with spaCy to identify entities like case numbers, statutes, and citations. The function should take the output from extract_text_from_pdf and return the processed text, ready for analysis. It's important that the preprocessing gracefully handles any peculiarities in the legal text.

Could you help me construct a function that accomplishes this? Sometimes the legal jargon throws unexpected curves, so the preprocessing needs to gracefully handle any peculiarities.