**Rewritten Code Request:**

We need to refactor the existing Python function `count_word_frequency` so that it can handle large text files efficiently without loading the entire file into memory. Specifically, we must:

1. Read the file line by line using a generator, rather than `f.read()`, to manage memory usage better.
2. Implement robust error handling for file operations, including managing exceptions for cases where the file might not exist or cannot be opened.

The current implementation is as follows (format the code neatly but **do not modify it**):

```python
def count_word_frequency(filename):
    word_counts = {}
    with open(filename, 'r') as f:
        text = f.read()
        words = text.split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    return word_counts
```