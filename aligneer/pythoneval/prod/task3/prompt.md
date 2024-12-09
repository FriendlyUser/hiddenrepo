so I've been tinkering with this data pipeline we're building it handles a pretty hefty amount of data,and while it's working okay,I can't shake the feeling that the code could be cleaner and more efficient.The function I'm particularly concerned about is the one responsible for data cleaning and normalization.Right now,it feels a bit convoluted,and I'm worried it won't scale well as our dataset grows.I'd love to get your thoughts on how to refactor it to improve performance and make it more modular,maybe even more Pythonic ? Also,if you see any potential pitfalls or better practices I should be following,please point them out.

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
we're aiming to handle much larger datasets in the near future,so scalability is definitely on my mind.Any suggestions on how to optimize this function for larger data volumes? Maybe using more efficient data structures or libraries?

