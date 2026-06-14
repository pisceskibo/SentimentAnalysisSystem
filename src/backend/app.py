# Libraries
from flask import Flask, request, jsonify
from flask_cors import CORS

from utils.validator import clean_and_validate_text
import pickle
import os

app = Flask(__name__)
CORS(app)

# Load Model
MODEL_PATH = "../../ai_models/tfidf_sentiment_model.pkl"

if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        saved_data = pickle.load(f)

    vectorizer = saved_data["vectorizer"]
    model = saved_data["model"]
else:
    raise FileNotFoundError("Không tìm thấy model.")


# Health Check
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "running",
        "service": "Sentiment Analysis API"
    })

# Predict API
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "status": "error",
            "message": "Payload JSON không hợp lệ."
        }), 400

    raw_text = data.get("text")

    cleaned_text, error_message = clean_and_validate_text(raw_text)

    if error_message:
        return jsonify({
            "status": "error",
            "message": error_message
        }), 422

    tfidf_vector = vectorizer.transform([cleaned_text])

    prediction = model.predict(tfidf_vector)[0]

    probabilities = model.predict_proba(tfidf_vector)[0]

    class_index = list(model.classes_).index(prediction)

    confidence_score = round(float(probabilities[class_index]), 4)

    return jsonify({
        "status": "success",
        "text": cleaned_text,
        "sentiment": prediction,
        "confidence_score": confidence_score
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)