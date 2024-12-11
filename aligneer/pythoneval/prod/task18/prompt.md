I'm working on a function that generates synthetic datasets with differential privacy guarantees, but I feel the current implementation isn't as efficient or readable as it could be.

import numpy as np

def generate_synthetic_data(original_data, epsilon):
    synthetic_data = []
    for row in original_data:
        noisy_row = []
        for value in row:
            noise = np.random.laplace(loc=0.0, scale=1/epsilon)
            noisy_value = value + noise
            noisy_row.append(noisy_value)
        synthetic_data.append(noisy_row)
    return synthetic_data
This works, but it's slow on large datasets and the nested loops make it hard to read. Could you help me refactor this to improve performance and modularity while still maintaining the necessary privacy protections?