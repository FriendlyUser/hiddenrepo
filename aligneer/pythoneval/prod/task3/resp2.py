from typing import Iterator, List
import re

def clean_text(text: str) -> str:
    """Clean a single text item by removing punctuation and standardizing format.
    
    Args:
        text: Input text string to clean
    
    Returns:
        Cleaned text string
    """
    return re.sub(r'[,.]', '', text.strip().lower())

def normalize_text(text: str) -> str:
    """Normalize a single text item by replacing spaces with underscores.
    
    Args:
        text: Input text string to normalize
    
    Returns:
        Normalized text string
    """
    return text.replace(' ', '_')

def process_data_stream(data: Iterator[str]) -> Iterator[str]:
    """Process data items one at a time using a generator.
    
    Args:
        data: Iterator of input text strings
    
    Yields:
        Processed text strings one at a time
    """
    for item in data:
        cleaned = clean_text(item)
        if cleaned:  # Skip empty strings
            yield normalize_text(cleaned)

def process_data(data: List[str]) -> List[str]:
    """Process a list of data items.
    
    Args:
        data: List of input text strings
    
    Returns:
        List of processed text strings
    """
    return list(process_data_stream(data))
