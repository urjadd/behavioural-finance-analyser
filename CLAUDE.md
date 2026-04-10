## Completed
- [x] Load dataset and inspect it (shape, columns, dtypes, nulls)
- [x] Clean the data (handle nulls, fix dtypes, rename columns)
- [x] EDA — asked and answered 3 business questions
- [x] Visualized spending patterns (categories, time of day, day of week, heatmaps)
- [x] Found 3 behavioural insights
- [x] Written findings in markdown
- [x] Stage 1 notebook complete

## Stage 2 — Data Science & ML ✅ COMPLETE

### Goal
Build a model that predicts spending category from transaction features

### Completed:
- [x] Defined ML problem — multi-class classification, target: category
- [x] Feature engineering — month, day, day_of_week, time_slice, is_weekend
- [x] Encoding — LabelEncoder for target, OneHot for categorical inputs
- [x] Ablation study — 4 datasets (flow vs signed, ordinal vs onehot)
- [x] Trained 4 models — DecisionTree, RandomForest, LogisticRegression, XGBoost
- [x] Evaluated — accuracy, confusion matrix, classification report
- [x] K-Fold cross validation with StratifiedKFold
- [x] Feature importance plot
- [x] Best model saved — XGBoost on signed_ordinal (81.40% accuracy)
- [x] Written findings and conclusions

### Key Learnings:
- [x] Encoding categorical variables (OneHotEncoder, LabelEncoder, OrdinalEncoder)
- [x] Ablation study for feature engineering decisions
- [x] Cross validation (StratifiedKFold)
- [x] Overfitting vs underfitting (single split vs K-Fold gap)
- [x] Feature importance (XGBoost)

### Best Model
XGBoost on signed_ordinal dataset — 81.40% accuracy
Saved to: models/best_model_xgb.pkl

---

## Stage 3 — Software Engineering (FastAPI + Docker) ⏳ Upcoming

### Goal
Serve the best model as a REST API and containerise with Docker

### TODO:
- [ ] Set up FastAPI project structure
- [ ] Build prediction endpoint — accepts transaction features, returns category
- [ ] Load saved model (joblib) inside FastAPI
- [ ] Test API locally
- [ ] Write Dockerfile
- [ ] Build and run Docker container
- [ ] Test containerised API

---

## Stage 4 — Cloud & Deployment ⏳ Upcoming
## Stage 5 — AI / Agentic Layer ⏳ Upcoming

---

| Stage | Focus | Status |
|-------|-------|--------|
| 1 | Data Foundations & EDA | ✅ Complete |
| 2 | Data Science & Machine Learning | ✅ Complete |
| 3 | Software Engineering — FastAPI + Docker | ⏳ Upcoming |
| 4 | Cloud & Deployment | ⏳ Upcoming |
| 5 | AI / Agentic Layer | ⏳ Upcoming |