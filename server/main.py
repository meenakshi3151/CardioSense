import joblib
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model = joblib.load('heart_disease_model.pkl')
FEATURES = [
    'Age',
    'Gender',
    'Diabetes',
    'Health-Insurance',
    'Blood-Rel-Stroke',
    'Vigorous-work',
    'Annual-Family-Income',
    'Uric.Acid',
    'Blood-Rel-Diabetes',
    'Glucose',
    'Creatinine',
    'Total-Cholesterol',
    'Glycohemoglobin',
    'Lymphocyte',
    'Platelet-count',
    'Cholesterol',
    'Moderate-work',
    'Red-Cell-Distribution-Width',
    'X60-sec-pulse',
    'HDL',
    'Diastolic',
    'Systolic',
    'Monocyte',
    'Eosinophils'
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to CardioSense!!"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400
        missing = [f for f in FEATURES if f not in data]
        if missing:
            return jsonify({"error": f"Missing features: {missing}"}), 400
        input_df = pd.DataFrame([data], columns=FEATURES)
        prediction = model.predict(input_df)[0]
        result = {
            "HeartDisease_Prediction": int(prediction)
        }
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
