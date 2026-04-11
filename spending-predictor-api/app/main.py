from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict_category

app = FastAPI(title = 'Spending Predictor API')

class Transaction(BaseModel):
    transaction_amount: float
    month: int
    day: int
    day_of_week_0: int
    day_of_week_1: int
    day_of_week_2: int
    day_of_week_3: int
    day_of_week_4: int
    day_of_week_5: int
    day_of_week_6: int
    time_slice: int

@app.post("/predict")
def predict(transaction: Transaction):
    features = [
        transaction.transaction_amount,
        transaction.month,
        transaction.day,
        transaction.day_of_week_0,
        transaction.day_of_week_1,
        transaction.day_of_week_2,
        transaction.day_of_week_3,
        transaction.day_of_week_4,
        transaction.day_of_week_5,
        transaction.day_of_week_6,
        transaction.time_slice,
    ]
    
    category = predict_category(features)
    return {"predicted_category": category}