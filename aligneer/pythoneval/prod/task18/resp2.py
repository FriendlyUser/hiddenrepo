import numpy as np

def generate_synthetic_data(original_data, epsilon, sensitivity=1.0):
    """
    Generate differentially private synthetic data using the Laplace mechanism.
    
    Args:
        original_data (np.ndarray): Input data matrix
        epsilon (float): Privacy parameter (ε > 0)
        sensitivity (float): Global sensitivity of the data (default=1.0)
    
    Returns:
        np.ndarray: Synthetic data with differential privacy guarantees
    """
    # Convert input to numpy array if it isn't already
    data = np.asarray(original_data)
    
    # Calculate Laplace noise scale (b = Δf/ε)
    scale = sensitivity / epsilon
    
    # Generate Laplace noise with same shape as input data
    noise = np.random.laplace(loc=0.0, scale=scale, size=data.shape)
    
    # Add noise to original data
    synthetic_data = data + noise
    
    return synthetic_data

original_data = np.array([[1, 2, 3],
                         [4, 5, 6]])
epsilon = 0.1
synthetic_data = generate_synthetic_data(original_data, epsilon)
print(synthetic_data)