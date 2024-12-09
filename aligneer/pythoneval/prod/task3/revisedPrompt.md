**Rewritten Prompt:**

I have a data processing function that currently cleans and normalizes incoming textual data, but I’m concerned about its scalability and overall efficiency as we handle larger datasets. Here is the original code segment:

```python
def process_data(data):
    cleaned_data = []
    for item in data:
        item = item.strip()
        item = item.lower()
        if item != '':
            item = item.replace(',', '')
            item = item.replace('.', '')
            cleaned_data.append(item)
    normalized_data = []
    for item in cleaned_data:
        norm_item = item
        if ' ' in item:
            words = item.split(' ')
            norm_item = '_'.join(words)
        normalized_data.append(norm_item)
    return normalized_data
```

I would like to refactor this function to improve its modularity, make it more Pythonic, and ensure it can scale better for much larger datasets. Specifically, I'm looking for:

1. Improved efficiency and memory usage (e.g., using generators or more efficient data structures).
2. Clearer separation of the cleaning and normalization steps into their own functions or modules.
3. Adherence to Python best practices and idiomatic patterns.

Please provide guidance on how best to refactor this code to handle larger datasets efficiently (e.g., using generators to minimize memory usage), and ensure the code follows best practices for scalability and modularity.