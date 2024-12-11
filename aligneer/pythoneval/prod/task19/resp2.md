To refactor the `count_word_frequency` function to handle large text files efficiently, we can read the file line by line using a generator. This approach will help manage memory usage better by not loading the entire file into memory at once. Additionally, we will add error handling to manage exceptions for cases where the file might not exist or cannot be opened. Here's the refactored implementation:

```python
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
```

### Key Changes:

1. **Line-by-Line Reading**: We use a `for` loop to iterate over each line in the file, which allows us to process the file incrementally without loading it entirely into memory.

2. **Error Handling**: 
   - We use a `try-except` block to catch `FileNotFoundError` if the file does not exist.
   - We also catch `IOError` to handle any other input/output errors that might occur while opening or reading the file.

This refactored function should be more efficient for large files and robust against common file operation errors.