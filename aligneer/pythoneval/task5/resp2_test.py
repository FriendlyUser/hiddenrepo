import pytest
from chatbot import process_user_message


# Test fixtures
@pytest.fixture
def setup_function():
    return process_user_message


# Basic functionality tests
def test_basic_input(setup_function):
    result = setup_function("I love programming!")
    assert isinstance(result, dict)
    assert 'entities' in result
    assert 'sentiment' in result
    assert isinstance(result['entities'], list)
    assert isinstance(result['sentiment'], dict)


# Input validation tests
def test_empty_string(setup_function):
    result = setup_function("")
    assert result['entities'] == []
    assert 'sentiment' in result


def test_none_input(setup_function):
    with pytest.raises(ValueError, match="Input must be a string"):
        setup_function(None)


def test_non_string_input(setup_function):
    with pytest.raises(ValueError, match="Input must be a string"):
        setup_function(123)


# Special characters and edge cases
def test_special_characters(setup_function):
    result = setup_function("Hello! @#$%^&* World")
    assert isinstance(result['entities'], list)
    assert 'sentiment' in result


def test_multiple_spaces(setup_function):
    result = setup_function("Hello  World")
    assert isinstance(result['entities'], list)


# Language-specific tests
def test_english_text(setup_function):
    result = setup_function("Apple Inc. is located in California.")
    assert any('Apple Inc.' in ent[0] for ent in result['entities'])
    assert any('California' in ent[0] for ent in result['entities'])


def test_mixed_language(setup_function):
    result = setup_function("Bonjour! My name is John.")
    assert isinstance(result['entities'], list)


# Entity recognition tests
def test_person_entity(setup_function):
    result = setup_function("Barack Obama was president.")
    assert any('Barack Obama' in ent[0] for ent in result['entities'])
    assert any('PERSON' in ent[1] for ent in result['entities'])


def test_organization_entity(setup_function):
    result = setup_function("Microsoft announced new products.")
    assert any('Microsoft' in ent[0] for ent in result['entities'])
    assert any('ORG' in ent[1] for ent in result['entities'])


# Sentiment analysis tests
def test_positive_sentiment(setup_function):
    result = setup_function("I'm really happy today!")
    assert result['sentiment']['label'] in ['POSITIVE', 'positive']


def test_negative_sentiment(setup_function):
    result = setup_function("This is terrible and disappointing.")
    assert result['sentiment']['label'] in ['NEGATIVE', 'negative']


# Long text tests
def test_long_text(setup_function):
    long_text = "This is a very long text. " * 50
    result = setup_function(long_text)
    assert isinstance(result['entities'], list)
    assert 'sentiment' in result


# Performance tests (optional)
@pytest.mark.performance
def test_processing_time(setup_function):
    import time
    start_time = time.time()
    setup_function("Quick test message")
    end_time = time.time()
    assert end_time - start_time < 5  # Should complete within 5 seconds