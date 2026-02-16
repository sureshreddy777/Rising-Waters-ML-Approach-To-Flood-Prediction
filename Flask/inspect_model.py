import joblib
import os
import sys

# Set paths
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'floods.save')
scaler_path = os.path.join(base_dir, 'transform.save')
output_file = os.path.join(base_dir, 'model_info.txt')

with open(output_file, 'w', encoding='utf-8') as f:
    def log(msg):
        print(msg)
        f.write(msg + '\n')

    try:
        log(f"Loading {model_path}...")
        model = joblib.load(model_path)
        log(f"\n--- Inspecting Model ---")
        log(f"Type: {type(model)}")
        
        if hasattr(model, 'n_features_in_'):
            log(f"n_features_in_: {model.n_features_in_}")
        
        if hasattr(model, 'feature_names_in_'):
            log(f"feature_names_in_: {model.feature_names_in_}")
        else:
            log("feature_names_in_: Not found (sklearn version mismatch?)")
            # Try XGBoost native
            if hasattr(model, 'get_booster'):
                try:
                    log(f"XGBoost feature names: {model.get_booster().feature_names}")
                except:
                    pass

        log(f"\nLoading {scaler_path}...")
        scaler = joblib.load(scaler_path)
        log(f"\n--- Inspecting Scaler ---")
        log(f"Type: {type(scaler)}")
        
        if hasattr(scaler, 'n_features_in_'):
            log(f"n_features_in_: {scaler.n_features_in_}")
        
        if hasattr(scaler, 'feature_names_in_'):
            log(f"feature_names_in_: {scaler.feature_names_in_}")
            
        if hasattr(scaler, 'mean_'):
            log(f"Scaler means: {scaler.mean_}")
        if hasattr(scaler, 'scale_'):
            log(f"Scaler scale: {scaler.scale_}")

    except Exception as e:
        log(f"Error: {e}")
        import traceback
        f.write(traceback.format_exc())
