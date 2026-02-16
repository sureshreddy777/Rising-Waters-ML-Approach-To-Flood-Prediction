from flask import Flask, render_template, request, jsonify
from joblib import load
import numpy as np
import os

app = Flask(__name__)

# Load the trained model and scaler
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'floods.save')
SCALER_PATH = os.path.join(os.path.dirname(__file__), 'transform.save')

model = load(MODEL_PATH)
scaler = load(SCALER_PATH)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/image')
def image():
    return render_template('image.html')

@app.route('/imageprediction')
def imageprediction():
    return render_template('imageprediction.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.get_json()
        
        # Extract features
        cloud_cover = float(data.get('cloud_cover', 0))
        annual_rainfall = float(data.get('annual_rainfall', 0))
        jan_feb_rainfall = float(data.get('jan_feb_rainfall', 0))
        march_may_rainfall = float(data.get('march_may_rainfall', 0))
        june_sep_rainfall = float(data.get('june_sep_rainfall', 0))
        
        # Create feature array
        features = np.array([[cloud_cover, annual_rainfall, jan_feb_rainfall, 
                            march_may_rainfall, june_sep_rainfall]])
        
        # Scale the features
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled)
        prediction_proba = model.predict_proba(features_scaled)
        
        # Determine flood risk level
        if prediction[0] == 1:
            risk_level = "High Risk - Flood Alert"
            confidence = float(prediction_proba[0][1]) * 100
        else:
            risk_level = "Low Risk - No Flood"
            confidence = float(prediction_proba[0][0]) * 100
        
        return jsonify({
            'success': True,
            'prediction': int(prediction[0]),
            'risk_level': risk_level,
            'confidence': float(round(confidence, 2))
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
