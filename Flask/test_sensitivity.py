import joblib
import numpy as np
import os

# Load model and scaler
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'floods.save')
scaler_path = os.path.join(base_dir, 'transform.save')
output_file = os.path.join(base_dir, 'sensitivity_results.txt')

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Base values (Means)
base_features = [36.28, 2925.48, 27.73, 377.25, 2022.84]

annual_steps = [3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400]

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("--- Sensitivity Analysis (Varying Annual Rainfall) ---\n")
    for annual in annual_steps:
        features_list = base_features.copy()
        features_list[1] = annual # Update Annual
        # Update Jun-Sep roughly proportional (approx 70% of annual)
        features_list[4] = annual * 0.7 
        
        features = np.array([features_list])
        features_scaled = scaler.transform(features)
        
        prediction = model.predict(features_scaled)
        prob = model.predict_proba(features_scaled)
        
        f.write(f"\nAnnual: {annual}, Jun-Sep: {features_list[4]}\n")
        f.write(f"Prediction: {prediction[0]}\n")
        f.write(f"Probabilities: {prob[0]}\n")
        f.write("-" * 20 + "\n")
