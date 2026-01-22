import joblib
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import numpy as np

class FifaValuePredictor:
    def __init__(self):
        self.model = None
        self.x_scaler = None
        self.y_scaler = None

    def load_assets(self, path="assets/fifa"):
        self.model = load_model(f"{path}_model.keras")
        self.x_scaler = joblib.load(f"{path}_x_scaler.pkl")
        self.y_scaler = joblib.load(f"{path}_y_scaler.pkl")

    def predict(self, features_list):
        input_data = np.array([features_list])
        X_scaled = self.x_scaler.transform(input_data)
        prediction = self.model.predict(X_scaled)
        return self.y_scaler.inverse_transform(prediction)