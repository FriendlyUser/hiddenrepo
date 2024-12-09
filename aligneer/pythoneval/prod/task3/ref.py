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