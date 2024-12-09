def clean_item(data):
    for item in data:
        item = item.strip().lower()
        if item:  # Check if the item is not an empty string
            item = item.replace(',', '').replace('.', '')
            yield item

def normalize_item(cleaned_data):
    for item in cleaned_data:
        if ' ' in item:
            words = item.split(' ')
            yield '_'.join(words)
        else:
            yield item

def process_data(data):
    cleaned_data = clean_item(data)
    normalized_data = normalize_item(cleaned_data)
    return list(normalized_data)

# Example usage
data = [
    "  Hello, World.  ",
    "Python Programming,  ",
    "",
    "Data Analysis.",
]

processed = process_data(data)
print(processed)