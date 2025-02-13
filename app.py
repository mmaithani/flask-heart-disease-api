import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load model & scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Define expected features
FEATURES = ["age", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        input_data = [data[feature] for feature in FEATURES]
        
        # Preprocess input
        input_data = np.array(input_data).reshape(1, -1)
        input_data = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0].tolist()

        return jsonify({
            "prediction": int(prediction),
            "probability": probability
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/", methods=["GET"])
def home():
    return "Heart Disease Prediction API is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

