def clean_item(item):
    """Cleans a single item by stripping whitespace, converting to lowercase, and removing punctuation."""
    item = item.strip().lower()
    if item:
        item = item.replace(',', '').replace('.', '')
    return item

def normalize_item(item):
    """Normalizes a single item by replacing spaces with underscores."""
    return '_'.join(item.split())

def process_data(data):
    """Processes data by cleaning and normalizing each item."""
    return (normalize_item(clean_item(item)) for item in data if clean_item(item))

# Example usage
data = ["  Hello, World!  ", "Python, is great.", "  ", "Data, Science."]
processed_data = process_data(data)

# Since processed_data is a generator, you can iterate over it or convert it to a list
for item in processed_data:
    print(item)
