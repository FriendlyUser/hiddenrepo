def count_word_frequency(filename):
    word_counts = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                words = line.split()
                for word in words:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: An error occurred while trying to read the file '{filename}'.")
    return word_counts

try:
    frequencies = count_word_frequency("sample.txt")
    print(frequencies)
except Exception as e:
    print(f"Error: {e}")