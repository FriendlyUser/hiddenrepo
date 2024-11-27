import pytest
from unittest.mock import patch

# Assuming the function is in a module named chatbot
from chatbot import process_user_message


# Mocking spaCy and HuggingFace Transformers
@pytest.fixture
def mock_spacy_and_transformers():
    with patch('chatbot.spacy.load') as mock_spacy_load, \
         patch('chatbot.pipeline') as mock_pipeline:

        # Mock spaCy NLP model
        mock_nlp = mock_spacy_load.return_value
        mock_nlp.return_value.ents = []

        # Mock HuggingFace sentiment analysis pipeline
        mock_classifier = mock_pipeline.return_value
        mock_classifier.return_value = [{'label': 'POSITIVE', 'score': 0.99}]

        yield mock_nlp, mock_classifier


def test_empty_input(mock_spacy_and_transformers):
    with pytest.raises(ValueError, match="Input must be a string."):
        process_user_message("")


def test_non_text_input(mock_spacy_and_transformers):
    with pytest.raises(ValueError, match="Input must be a string."):
        process_user_message(123)


def test_spe_cha(mock_spacy_and_transformers):
    result = process_user_message("!@#$%^&*()")
    assert result['entities'] == []
    assert result['sentiment']['label'] == 'POSITIVE'


def test_diff_lan(mock_spacy_and_transformers):
    result = process_user_message("Bonjour, je m'appelle AI.")
    assert result['entities'] == []
    assert result['sentiment']['label'] == 'POSITIVE'


def test_english_text(mock_spacy_and_transformers):
    result = process_user_message("Hello, my name is AI.")
    assert result['entities'] == []
    assert result['sentiment']['label'] == 'POSITIVE'


def test_entities_extraction(mock_spacy_and_transformers):
    mock_nlp, _ = mock_spacy_and_transformers
    mock_nlp.return_value.ents = [
        type('MockEntity', (object,), {'text': 'AI', 'label_': 'ORG'})()
    ]
    result = process_user_message("AI is a powerful tool.")
    assert result['entities'] == [('AI', 'ORG')]
    assert result['sentiment']['label'] == 'POSITIVE'

if __name__ == "__main__":
    # Run the tests when the script is executed
    pytest.main()