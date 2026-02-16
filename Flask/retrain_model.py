import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# Set paths
base_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(base_dir, '../Dataset/flood_dataset.xlsx')
model_path = os.path.join(base_dir, 'floods.save')
scaler_path = os.path.join(base_dir, 'transform.save')

print(f"Loading dataset from {dataset_path}...")
df = pd.read_excel(dataset_path)

# Features and Target
# Based on previous inspection, features are:
features = ['Cloud Cover', 'ANNUAL', 'Jan-Feb', 'Mar-May', 'Jun-Sep']
target = 'flood'

X = df[features]
y = df[target]

print("Features:", list(X.columns))
print("Class Distribution:\n", y.value_counts())

# Calculate scale_pos_weight for imbalance handling
# scale_pos_weight = count(negative examples) / count(positive examples)
neg_count = y.value_counts()[0]
pos_count = y.value_counts()[1]
scale_weight = neg_count / pos_count
print(f"Calculated scale_pos_weight: {scale_weight:.2f}")

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scaling
print("Scaling features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model Training
print("Training XGBClassifier with class balancing...")
model = XGBClassifier(
    scale_pos_weight=scale_weight,
    eval_metric='logloss',
    use_label_encoder=False,
    random_state=42
)
model.fit(X_train_scaled, y_train)

# Evaluation
y_pred = model.predict(X_test_scaled)
print("\n--- Model Performance ---")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Saving
print(f"Saving model to {model_path}...")
joblib.dump(model, model_path)
print(f"Saving scaler to {scaler_path}...")
joblib.dump(scaler, scaler_path)

print("Retraining Complete!")
