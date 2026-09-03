# Personal Finance Behaviour Analyser

> Analysing human spending patterns through data — from raw transactions to a deployed AI-powered product.

---

## Project Overview

This project explores **behavioural finance** — the intersection of psychology and personal finance — by analysing real-world transaction data to uncover how and why people spend the way they do.

Built across 6 stages, it grows from a data analysis notebook into a fully deployed AI product with a live API, Docker container, LLM agent, and interactive frontend.

---

## Live Demo

API Endpoint: `https://behavioural-finance-analyser.onrender.com/predict`

---

## Roadmap

| Stage | Focus | Status |
|-------|-------|--------|
| 1 | Data Foundations & EDA | ✅ Complete |
| 2 | Data Science & Machine Learning | ✅ Complete |
| 3 | Software Engineering - FastAPI + Docker | ✅ Complete |
| 4 | Cloud & Deployment | ✅ Complete |
| 5 | AI / Agentic Layer | ✅ Complete |
| 6 | Frontend UI | ✅ Complete |

---

## Project Structure

```
behavioural-finance-analyser/
├── notebooks/
│   ├── 01_EDA_initial_analysis.ipynb
│   └── 02_ML_classification.ipynb
├── data/
│   ├── raw/                        ← Original dataset
│   └── processed/                  ← Cleaned data
├── models/
│   ├── best_model_xgb.pkl          ← Trained XGBoost model
│   └── label_encoder.pkl           ← Category label encoder
├── spending-predictor-api/         ← FastAPI + Docker
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── model.py
│   ├── models/
│   │   ├── best_model_xgb.pkl
│   │   └── label_encoder.pkl
│   ├── requirements.txt
│   └── Dockerfile
├── spending-agent/                 ← LLM agent + Streamlit UI
│   ├── agent.py
│   ├── app.py
│   └── requirements.txt
├── docs/                           ← Findings and reports
├── outputs/                        ← Charts and visualisations
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## How It Works

1. User describes a transaction in plain English
2. Groq LLM extracts features from the text
3. Features are sent to the FastAPI prediction endpoint on Render
4. XGBoost model predicts the spending category
5. LLM generates a personalised financial insight
6. Result is displayed in the Streamlit UI

---

## Stage Summaries

### Stage 1 - Data Foundations & EDA
Loaded and cleaned real transaction data. Explored spending patterns by category, time of day, and day of week. Uncovered 3 behavioural insights about spending behaviour.

### Stage 2 - Machine Learning
Built a multi-class classifier to predict spending category. Compared DecisionTree, RandomForest, LogisticRegression, and XGBoost across ablation datasets. Best model: XGBoost with 74.31% K-Fold accuracy.

### Stage 3 - FastAPI + Docker
Wrapped the model in a REST API using FastAPI. Containerised with Docker for reproducible deployment. Tested via Swagger UI.

### Stage 4 - Cloud Deployment
Deployed the Docker container to Render. Live API accessible at a public URL.

### Stage 5 - AI / Agentic Layer
Built a natural language agent using Groq LLM. User types a plain English transaction description. Agent extracts features, calls the API, and returns a spending insight.

### Stage 6 - Frontend UI
Built a Streamlit frontend with a dark theme UI. Users can interact with the agent directly in a browser without touching the terminal.

---

## Tech Stack

| Layer | Tools |
|-------|-------|
| Data & ML | Python, pandas, numpy, scikit-learn, XGBoost |
| API | FastAPI, Uvicorn, Pydantic |
| Containerisation | Docker |
| Cloud | Render |
| LLM | Groq, Llama 3.3 70B |
| Frontend | Streamlit |
| Visualisation | matplotlib, seaborn, plotly |

---

## Setup

```powershell
# Clone the repo
git clone https://github.com/urjadd/behavioural-finance-analyser.git
cd behavioural-finance-analyser

# Activate virtual environment
venv/Scripts/Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

To run the Streamlit app locally:

```powershell
cd spending-agent
streamlit run app.py
```

Create a `.env` file in the root with:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## About

Built as part of a personal upskilling journey in the direction of AI, data, and finance. This project serves as a portfolio piece demonstrating end to end ML engineering: from raw data to a deployed, user-facing AI product.
