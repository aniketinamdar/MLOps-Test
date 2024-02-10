import joblib
import numpy as np
import pandas as pd
import pathlib as Path

from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        model_path = Path('artifacts/model_trainer/model.joblib')
        print(f"Loading model from: {model_path.absolute()}")
        if model_path.exists():
            self.model = joblib.load(model_path)
            print("Model loaded successfully.")
        else:
            print("Model file not found.")

    def predict(self, data):
        prediction = self.model.predict(data)
        return prediction