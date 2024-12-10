from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Define expected input shape
INPUT_SHAPE = (10,)  # Expecting 10 features

# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=INPUT_SHAPE),
    tf.keras.layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if request contains JSON data
        if not request.is_json:
            return jsonify({
                'error': 'Invalid request format. Expected JSON data.'
            }), 400

        # Get JSON data
        data = request.get_json()
        
        # Validate that data is not None
        if data is None:
            return jsonify({
                'error': 'Empty request body'
            }), 400

        # Convert to numpy array and validate shape
        try:
            data_input = np.array([data])
            
            # Check if input has correct number of features
            if data_input.shape[1] != INPUT_SHAPE[0]:
                return jsonify({
                    'error': f'Invalid input shape. Expected {INPUT_SHAPE[0]} features, but got {data_input.shape[1]}'
                }), 400

            # Validate data type
            if not np.issubdtype(data_input.dtype, np.number):
                return jsonify({
                    'error': 'Input data must contain only numerical values'
                }), 400

        except ValueError as ve:
            return jsonify({
                'error': f'Error processing input data: {str(ve)}'
            }), 400

        # Make prediction
        try:
            prediction = model.predict(data_input)
            return jsonify({
                'success': True,
                'prediction': prediction.tolist(),
                'input_shape': data_input.shape
            })

        except Exception as e:
            return jsonify({
                'error': f'Prediction error: {str(e)}'
            }), 500

    except Exception as e:
        return jsonify({
            'error': f'Server error: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
