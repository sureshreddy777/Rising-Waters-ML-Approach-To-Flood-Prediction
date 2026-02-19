# Flood Risk Prediction System 🌊

A comprehensive machine learning-based system designed to predict the likelihood of floods based on historical rainfall data. This project encompasses the entire pipeline from data analysis and model training to a user-friendly web interface for real-time predictions.

## 🚀 Overview

The Flood Risk Prediction System aims to provide an accessible tool for early flood detection. By analyzing key meteorological factors such as cloud cover and seasonal rainfall, the system predicts whether an area is at high or low risk of flooding.

🎥 **Watch the project demo video:**  
👉 https://drive.google.com/file/d/1IteuJyyjQ6gliBuJDW-CFIEaV52rp71e/view?usp=sharing

## 📂 Project Structure

```bash
ProjectFiles/
├── Dataset/
│   └── flood_dataset.xlsx      # Historical rainfall and flood data
├── Training/
│   └── Floods.ipynb            # Jupyter Notebook for EDA & Model Training
├── Flask/
│   ├── app.py                  # Main Flask application
│   ├── floods.save             # Trained Machine Learning Model (XGBoost/Pickle)
│   ├── transform.save          # Scaler object for data normalization
│   ├── requirements.txt        # Python dependencies for the web app
│   ├── static/                 # CSS, JavaScript, and images
│   └── templates/              # HTML templates for the web interface
├── documentation/              # Project reports and documentation (Phase 1-4)
└── Screenshots/                # Application screenshots and demo images
```

## ✨ Features

*   **Accurate Predictions**: Utilizes advanced machine learning algorithms (XGBoost, Random Forest accuracy ~99.3%) trained on historical weather data.
*   **Interactive Web Interface**: A responsive and user-friendly web app built with Flask and Bootstrap 5.
*   **Real-time Risk Assessment**: Instant feedback on flood risk levels based on user input for diverse parameters.
*   **Data Visualization**: Insightful analysis of rainfall patterns provided in the training notebooks.

## 🛠️ Tech Stack

*   **Language**: Python 3.8+
*   **Web Framework**: Flask
*   **Machine Learning**: Scikit-learn, XGBoost, Pandas, NumPy
*   **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
*   **Tools**: Jupyter Notebook, VS Code

## ⚙️ How to Run

### Prerequisite: Setup Environment
It is recommended to use of a virtual environment to manage dependencies.
```bash
python -m venv venv
# Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
```

### 1. Model Training (Optional)
If you wish to retrain the model or explore the data:
1.  Navigate to the `Training` directory.
2.  Open `Floods.ipynb` using Jupyter Notebook or JupyterLab.
3.  Run the cells to perform data analysis and train the models.
4.  The trained model (`floods.save`) and scaler (`transform.save`) will be saved. Copy them to the `Flask` directory if you want to update the web app with the new model.

### 2. Running the Web Application
To launch the prediction interface:
1.  Navigate to the `Flask` directory:
    ```bash
    cd Flask
    ```
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Start the Flask server:
    ```bash
    python app.py
    ```
4.  Open your web browser and go to:
    `http://127.0.0.1:5000/`

## 📊 Inputs Needed
The system predicts flood risk based on the following parameters:
*   **Cloud Cover**: Percentage of cloud cover (0-100%).
*   **Annual Rainfall**: Total annual rainfall in mm.
*   **Jan-Feb Rainfall**: Rainfall during winter months (mm).
*   **March-May Rainfall**: Rainfall during pre-monsoon season (mm).
*   **June-Sept Rainfall**: Rainfall during the monsoon season (mm).

## 📝 License
This project is developed for educational and research purposes.

