import joblib
import numpy as np

model = joblib.load("models/best_model_xgb.pkl")
CATEGORY_MAP = {
    0: "Food",
    1: "Household",
    2: "Other",
    3: "Salary",
    4: "Transportation"
}

def predict_category(features: list):
    prediction = model.predict(np.array([features]))
    category = CATEGORY_MAP[int(prediction[0])]
    return category