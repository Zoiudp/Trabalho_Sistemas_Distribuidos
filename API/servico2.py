# Flask app code (api_app.py)
import os
from flask import Flask, jsonify
from inference_yolo import predict_disease
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.route('/inferencia_chat', methods=['POST'])
def post_data():
    data = request.get_json()
    data = data.get('chat')
    model_path = r'Pre_processing&Model_Training\coffee_disease_model.pt'
    conf_threshold = 0.8

    result = predict_disease(model_path, conf_threshold, display_image=False, no_image=True, chat_message=data)

    return jsonify({'chat': result.get('description')})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
