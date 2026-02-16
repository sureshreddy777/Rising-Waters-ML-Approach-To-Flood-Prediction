import joblib
import numpy as np
import os
import pandas as pd

# Load model and scaler
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'floods.save')
scaler_path = os.path.join(base_dir, 'transform.save')
output_file = os.path.join(base_dir, 'prediction_results.txt')

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Define test cases
test_cases = [
    {
        "name": "Average Values",
        "features": [36.28, 2925.48, 27.73, 377.25, 2022.84]
    },
    {
        "name": "Extreme High Rainfall",
        "features": [44.0, 5000.0, 100.0, 1000.0, 4000.0]
    },
    {
        "name": "Max Values from Dataset",
        "features": [44.0, 4257.8, 98.1, 915.2, 3451.3]
    }
]

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("--- Prediction Results ---\n")
    for case in test_cases:
        features = np.array([case["features"]])
        # Scale features
        features_scaled = scaler.transform(features)
        
        # Predict
        prediction = model.predict(features_scaled)
        prob = model.predict_proba(features_scaled)
        
        f.write(f"\nCase: {case['name']}\n")
        f.write(f"Input: {case['features']}\n")
        f.write(f"Prediction: {prediction[0]}\n")
        f.write(f"Probabilities: {prob[0]}\n")
        f.write("-" * 30 + "\n")
