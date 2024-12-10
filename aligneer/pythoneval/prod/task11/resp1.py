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
    try:
        data = request.get_json()
        
        # Check if data is a list and has the correct number of features
        if not isinstance(data, list) or len(data) != 10:
            return jsonify({'error': 'Input data must be a list of 10 numbers.'}), 400
        
        # Ensure the input data is a NumPy array with the correct shape
        data_input = np.array([data])
        
        # Make a prediction
        prediction = model.predict(data_input)
        
        return jsonify({'prediction': prediction.tolist()})
    
    except Exception as e:
        # Catch any exceptions and return an error message
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)