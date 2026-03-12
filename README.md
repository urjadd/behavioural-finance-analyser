# Personal Finance Behaviour Analyser

> Analysing human spending patterns through data — from raw transactions to behavioural insights.

---

## Project Overview

This project explores **behavioural finance** — the intersection of psychology and personal finance — by analysing real-world transaction data to uncover how and why people spend the way they do.

It is a **long-term, evolving project** built across 5 stages: starting as a data analysis project and growing into a fully deployed AI-powered product.

---

## Roadmap

| Stage | Focus | Status |
|-------|-------|--------|
| 1 | Data Foundations & EDA | 🔄 In Progress |
| 2 | Data Science & Machine Learning | ⏳ Upcoming |
| 3 | Software Engineering — FastAPI + Docker | ⏳ Upcoming |
| 4 | Cloud & Deployment | ⏳ Upcoming |
| 5 | AI / Agentic Layer | ⏳ Upcoming |

---

## Project Structure

```
personal-finance-behaviour-analyser/
├── src/               ← Source code
├── tests/             ← Unit tests
├── data/
│   ├── raw/           ← Original dataset (never modified)
│   └── processed/     ← Cleaned, transformed data
├── notebooks/         ← Jupyter EDA notebooks
├── docs/              ← Findings, reports, documentation
├── outputs/           ← Charts, visualisations
├── models/            ← Trained ML models (Stage 2+)
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Stage 1 — Data Foundations & EDA

**Goal:** Load, clean, and explore transaction data to find meaningful spending patterns and behavioural insights.

### Key Questions Being Explored
- Where does the most money go? (by category, time period)
- Are there seasonal or monthly spending trends?
- What does "abnormal" spending look like in this dataset?
- Can we identify impulsive vs. planned spending behaviour?
- What 3 behavioural insights can we extract from the data?

### Deliverables
- [ ] Cleaned dataset in `data/processed/`
- [ ] EDA notebook in `notebooks/`
- [ ] Visualisations in `outputs/`
- [ ] Findings summary in `docs/`

---

## Tech Stack

**Stage 1**
- Python 3.11.9
- pandas, numpy
- matplotlib, seaborn, plotly
- Jupyter Notebook

**Later Stages (planned)**
- FastAPI, Docker
- AWS / GCP
- LangChain / LLM APIs

---

## Setup

```powershell
# Clone the repo
git clone https://github.com/YOUR_USERNAME/personal-finance-behaviour-analyser.git
cd personal-finance-behaviour-analyser

# Activate virtual environment (Windows PowerShell)
d:/Upskilling/Projects/behavioural-finance-analyser/venv/Scripts/Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

---

## About

Built as part of a personal upskilling journey transitioning from **Data → Forward Development Engineer**, with a focus on Finance + AI.

This project serves as a portfolio centrepiece, evolving from exploratory analysis into a production-ready AI product.
