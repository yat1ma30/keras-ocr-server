from flask import Flask, request, jsonify
import keras_ocr
import base64
import cv2
import numpy as np
from flask_cors import CORS
import traceback

app = Flask(__name__)
CORS(app)  # Enable CORS

# Initialize Keras-OCR model
pipeline = keras_ocr.pipeline.Pipeline()


@app.route('/ocr', methods=['POST'])
def ocr_image():
    try:
        # Decode Base64 data
        image_data = base64.b64decode(request.json['image'])
        # Convert the image to a NumPy array
        nparr = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # Perform OCR on the image using Keras-OCR
        prediction_groups = pipeline.recognize([image])
        # Convert the results to JSON
        results = [prediction[0] for prediction in prediction_groups[0]]
        return jsonify({'results': results})
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
