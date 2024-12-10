from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')
@app.route('/predict', methods=['POST'])
def predict():
    # Check if JSON data is provided
    if not request.is_json:
        return jsonify({'error': 'Request must be in JSON format'}), 400

    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    try:
        # Convert data to a NumPy array and ensure it has the correct shape
        data_input = np.array(data, dtype=np.float32)

        # Reshape to match the expected input shape of the model
        if data_input.ndim == 1:
            data_input = np.expand_dims(data_input, axis=0)  # Add batch dimension

        # Validate the shape
        if data_input.shape[1] != 10:
            return jsonify({'error': f'Invalid input shape. Expected 10 features, got {data_input.shape[1]}'}), 400

        prediction = model.predict(data_input)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': f'Processing failed: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)