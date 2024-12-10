import horovod.torch as hvd
import numpy as np

def some_processing_function(value):
    # Dummy processing function
    return value * 2

def preprocess_data(data):
    # Initialize Horovod
    hvd.init()
    
    # Get the rank and size
    rank = hvd.rank()
    size = hvd.size()
    
    # Split the data among workers
    data_split = np.array_split(data, size)
    
    # Each worker processes its portion of the data
    local_data = data_split[rank]
    local_processed = []
    for item in local_data:
        # Assume 'item' is a dictionary with nested keys
        value = item['features']['value']
        # Perform some processing
        result = some_processing_function(value)
        local_processed.append(result)
    
    # Gather the processed results from all workers
    processed = hvd.allgather_object(local_processed)
    
    return processed

# Example usage
if __name__ == "__main__":
    # Sample data
    data = [{'features': {'value': i}} for i in range(100)]
    
    # Preprocess data
    processed_data = preprocess_data(data)
    
    # Only print on one worker to avoid duplicate outputs
    if hvd.rank() == 0:
        print(processed_data)