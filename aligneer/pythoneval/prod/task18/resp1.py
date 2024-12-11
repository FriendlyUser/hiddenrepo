import numpy as np

def add_laplace_noise(data, epsilon):
    """
    Adds Laplace noise to the data for differential privacy.

    Parameters:
    - data: NumPy array of original data.
    - epsilon: Privacy parameter.

    Returns:
    - Noisy data as a NumPy array.
    """
    scale = 1 / epsilon
    noise = np.random.laplace(loc=0.0, scale=scale, size=data.shape)
    return data + noise

def generate_synthetic_data(original_data, epsilon):
    """
    Generates synthetic data with differential privacy guarantees.

    Parameters:
    - original_data: 2D list or NumPy array of original data.
    - epsilon: Privacy parameter.

    Returns:
    - Synthetic data as a NumPy array.
    """
    original_data = np.array(original_data)  # Ensure input is a NumPy array
    synthetic_data = add_laplace_noise(original_data, epsilon)
    return synthetic_data

original_data = np.array([[1, 2, 3],
                         [4, 5, 6]])
epsilon = 0.1
synthetic_data = generate_synthetic_data(original_data, epsilon)
print(synthetic_data)