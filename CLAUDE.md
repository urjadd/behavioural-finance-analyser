## Stage 1 - Data Foundations & EDA ✅ COMPLETE

### Completed:
- [x] Load dataset and inspect it (shape, columns, dtypes, nulls)
- [x] Clean the data (handle nulls, fix dtypes, rename columns)
- [x] EDA - asked and answered 3 business questions
- [x] Visualized spending patterns (categories, time of day, day of week, heatmaps)
- [x] Found 3 behavioural insights
- [x] Written findings in markdown
- [x] Stage 1 notebook complete

---

## Stage 2 - Data Science & ML ✅ COMPLETE

### Goal
Build a model that predicts spending category from transaction features

### Completed:
- [x] Defined ML problem - multi-class classification, target: category
- [x] Feature engineering - month, day, day_of_week, time_slice, is_weekend
- [x] Encoding - LabelEncoder for target, OneHot for categorical inputs
- [x] Ablation study - 4 datasets (flow vs signed, ordinal vs onehot)
- [x] Trained 4 models - DecisionTree, RandomForest, LogisticRegression, XGBoost
- [x] Evaluated - accuracy, confusion matrix, classification report
- [x] K-Fold cross validation with StratifiedKFold
- [x] Feature importance plot
- [x] Best model saved - XGBoost on signed_ordinal
- [x] Written findings and conclusions

### Key Learnings:
- [x] Encoding categorical variables (OneHotEncoder, LabelEncoder, OrdinalEncoder)
- [x] Ablation study for feature engineering decisions
- [x] Cross validation (StratifiedKFold)
- [x] Overfitting vs underfitting (single split vs K-Fold gap)
- [x] Feature importance (XGBoost)

### Best Model
XGBoost on signed_ordinal dataset
- Single split accuracy: 81.40%
- K-Fold accuracy: 74.31%
- Model selected based on K-Fold (more reliable than single split)
- time_slice excluded as it did not consistently improve performance across folds

Saved to: models/best_model_xgb.pkl

### Model Input Features (11):
transaction_amount (signed), month, day, day_of_week_0-6, time_slice

### Category Mapping:
0: Food, 1: Household, 2: Other, 3: Salary, 4: Transportation

---

## Stage 3 - Software Engineering (FastAPI + Docker) ✅ COMPLETE

### Goal
Serve the best model as a REST API and containerise with Docker

### Completed:
- [x] Set up FastAPI project structure (spending-predictor-api/)
- [x] Written requirements.txt with pinned versions
- [x] Built model.py - loads XGBoost model, predicts category
- [x] Built main.py - FastAPI app with /predict endpoint
- [x] Pydantic schema for request validation (Transaction class)
- [x] Tested API locally with uvicorn
- [x] Tested /predict endpoint via /docs (Swagger UI)
- [x] Written Dockerfile
- [x] Built Docker image
- [x] Ran Docker container
- [x] Tested containerised API

### Project Structure:
```
spending-predictor-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── model.py
├── models/
│   ├── best_model_xgb.pkl
│   └── label_encoder.pkl
├── requirements.txt
└── Dockerfile
```

### Key Learnings:
- [x] FastAPI - backend framework for building APIs
- [x] Uvicorn - ASGI server (mediator between network and FastAPI)
- [x] Pydantic - request validation and type checking
- [x] Docker - containerisation for reproducible deployments
- [x] Dockerfile - recipe to build a container image
- [x] Debugging numpy type serialisation issues with FastAPI

### Tech Stack:
fastapi==0.135.3, uvicorn==0.44.0, joblib==1.5.3, xgboost==3.2.0, scikit-learn==1.8.0, pandas==3.0.1

---

## Stage 4 - Cloud & Deployment ⏳ Upcoming

### Goal
Deploy the Docker container to the cloud so the API is accessible via a public URL

### TODO:
- [ ] Choose cloud platform (Render / Railway / AWS / GCP)
- [ ] Deploy Docker container
- [ ] Get a public API URL
- [ ] Test the deployed API

---

## Stage 5 - AI / Agentic Layer ⏳ Upcoming

### Goal
Add an AI layer so users can interact with the API using natural language

### TODO:
- [ ] Integrate LLM to parse natural language into transaction features
- [ ] Build agent that calls the prediction API
- [ ] Test end-to-end natural language predictions

---

## Stage 6 - Frontend UI ⏳ Upcoming

### Goal
Build a user-facing web interface for the spending predictor

### TODO:
- [ ] Choose framework (Streamlit / React / HTML+JS)
- [ ] Build UI for transaction input and prediction display
- [ ] Connect frontend to the API
- [ ] Deploy frontend

---

| Stage | Focus | Status |
|-------|-------|--------|
| 1 | Data Foundations & EDA | ✅ Complete |
| 2 | Data Science & Machine Learning | ✅ Complete |
| 3 | Software Engineering - FastAPI + Docker | ✅ Complete |
| 4 | Cloud & Deployment | ⏳ Upcoming |
| 5 | AI / Agentic Layer | ⏳ Upcoming |
| 6 | Frontend UI | ⏳ Upcoming |