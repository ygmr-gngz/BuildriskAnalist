import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import joblib
import pandas as pd
from interfaces.IRiskModel import IRiskModel

class XGBRiskModel(IRiskModel):
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None

    def load_model(self):
        """Pickle dosyasından modeli yükler"""
        self.model = joblib.load(self.model_path)

    def predict(self, data: pd.DataFrame):
        """Model ile tahmin yapar"""
        if self.model is None:
            raise ValueError("Model yüklenmedi. Önce load_model() çağır.")
        return self.model.predict(data)