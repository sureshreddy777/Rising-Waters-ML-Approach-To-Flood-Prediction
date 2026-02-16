# Floods Prediction Web Application

A Flask-based web application for flood prediction using machine learning models.

## Project Structure

```
Flask/
├── app.py                          # Main Flask application
├── floods.save                     # Trained XGBoost model
├── transform.save                  # StandardScaler for feature scaling
├── requirements.txt                # Python dependencies
├── templates/
│   ├── home.html                  # Main prediction page
│   ├── intro.html                 # Introduction page
│   ├── image.html                 # Dataset information
│   └── imageprediction.html       # Model details page
└── static/
    ├── css/
    │   └── styles.css             # Global styles
    └── js/
        └── main.js                # Form handling and AJAX
```

## Features

- **User-friendly Interface**: Bootstrap-based responsive design
- **Real-time Predictions**: AJAX form submission with instant results
- **Model Information**: Detailed pages about the model and dataset
- **Multiple ML Models**: Trained with Decision Tree, Random Forest, KNN, and XGBoost
- **Feature Scaling**: Automatic feature normalization using sklearn's StandardScaler
- **Risk Assessment**: Displays flood risk level and confidence scores

## Installation

1. Install Python 3.8+ on your system
2. Navigate to the Flask directory:
   ```bash
   cd Flask
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

4. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Make sure you're in the Flask directory
2. Run the Flask app:
   ```bash
   python app.py
   ```

3. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Input Parameters

The model expects 5 meteorological features:

1. **Cloud Cover Percentage** (0-100%): Sky coverage by clouds
2. **Annual Rain Fall** (mm): Total yearly precipitation
3. **Jan-Feb Rainfall** (mm): Precipitation during January-February
4. **March-May Rainfall** (mm): Precipitation during March-May
5. **June-September Rainfall** (mm): Precipitation during June-September

## Prediction Output

- **Risk Level**: High Risk or Low Risk classification
- **Confidence Score**: Probability percentage (0-100%)
- **Visual Alert**: Color-coded alert (red for flood risk, green for safe)

## Technical Details

### Models Used
- **XGBoost** (Primary): Gradient boosting classifier with superior accuracy
- **Random Forest**: Ensemble method with multiple decision trees
- **Decision Tree**: Simple tree-based classifier
- **K-Nearest Neighbors**: Instance-based learning

### Data Processing
- Features are scaled using StandardScaler before prediction
- All input values are normalized to match training data distribution
- Binary classification: 1 = Flood likely, 0 = No flood

### Performance Metrics
- Accuracy: Overall correctness
- Precision: True positive rate among predicted positives
- Recall: True positive rate among actual positives
- Confusion Matrix: Classification performance visualization

## Pages

1. **Home** (`/`): Main prediction interface
2. **Introduction** (`/intro`): Information about the system
3. **Dataset** (`/image`): Dataset overview and statistics
4. **Model Details** (`/imageprediction`): Machine learning models explanation

## Dependencies

- **Flask**: Web framework
- **NumPy**: Numerical computing
- **Pandas**: Data manipulation
- **joblib**: Model and scaler serialization
- **scikit-learn**: Machine learning utilities
- **XGBoost**: Gradient boosting framework
- **Bootstrap 5**: Frontend framework (via CDN)

## Troubleshooting

### Model file not found
Ensure `floods.save` and `transform.save` are in the Flask directory.

### Port already in use
Change the port in app.py:
```python
app.run(debug=True, port=5001)
```

### Module import errors
Reinstall dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

## API Endpoint

### POST /predict
Sends prediction request with feature values.

**Request Body (JSON):**
```json
{
    "cloud_cover": 65.5,
    "annual_rainfall": 1200.0,
    "jan_feb_rainfall": 150.0,
    "march_may_rainfall": 200.0,
    "june_sep_rainfall": 500.0
}
```

**Response:**
```json
{
    "success": true,
    "prediction": 1,
    "risk_level": "High Risk - Flood Alert",
    "confidence": 85.23
}
```

## Future Enhancements

- Database integration for historical predictions
- User authentication
- Batch predictions support
- Advanced visualizations
- Real-time data integration
- Mobile application version

## License

This project is for educational purposes.

## Support

For issues or questions, refer to the documentation or check the individual sections in the application.
