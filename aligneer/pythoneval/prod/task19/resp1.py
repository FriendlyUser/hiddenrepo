def count_word_frequency(filename):
    """
    Count word frequencies in a text file using memory-efficient line-by-line processing.
    
    Args:
        filename (str): Path to the text file
        
    Returns:
        dict: Dictionary containing word frequencies
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
        IOError: If there's an error reading the file
        UnicodeDecodeError: If the file encoding is not compatible
    """
    word_counts = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Process the file line by line using a generator
            for line in file:
                # Split the line into words
                words = line.strip().split()
                
                # Update word frequencies
                for word in words:
                    word_counts[word] = word_counts.get(word, 0) + 1
                    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' was not found.")
    except IOError as e:
        raise IOError(f"Error reading file '{filename}': {str(e)}")
    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(f"Error decoding file '{filename}': {str(e)}")
    
    return word_counts

try:
    frequencies = count_word_frequency("sample.txt")
    print(frequencies)
except Exception as e:
    print(f"Error: {e}")