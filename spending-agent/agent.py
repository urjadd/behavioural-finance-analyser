from groq import Groq
import json
import os
import requests
import time
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL_NAME = "llama-3.3-70b-versatile"

API_URL = "https://behavioural-finance-analyser.onrender.com/predict"


def safe_generate(prompt):

    retries = 3
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content.strip()

        except Exception:
            wait_time = (attempt + 1) * 5
            print(
                f"Retry {attempt+1}/{retries} "
                f"after {wait_time}s..."
            )

            time.sleep(wait_time)

    raise RuntimeError(
        "LLM failed after retries"
    )

def extract_or_ask(user_input, asked_already=False):
    if asked_already:
        prompt = f"""
A user described a transaction:
"{user_input}"

Make reasonable assumptions for any missing details.
Accept any date format (DD/MM/YYYY, "2nd feb", "feb 2", etc).
Automatically calculate day_of_week_0 through day_of_week_6 from the date.

Return ONLY valid JSON with these exact keys:
{{
  "transaction_amount": float (positive=income, negative=expense),
  "month": int (1-12),
  "day": int (1-31),
  "day_of_week_0": int (1 if Monday else 0),
  "day_of_week_1": int (1 if Tuesday else 0),
  "day_of_week_2": int (1 if Wednesday else 0),
  "day_of_week_3": int (1 if Thursday else 0),
  "day_of_week_4": int (1 if Friday else 0),
  "day_of_week_5": int (1 if Saturday else 0),
  "day_of_week_6": int (1 if Sunday else 0),
  "time_slice": int (morning 6-11=0, afternoon 12-16=1, evening 17-21=2, night=3)
}}
Return ONLY JSON. No explanation. No markdown.
"""
    else:
        prompt = f"""
A user described a transaction:
"{user_input}"

Check if these details exist or can be inferred:
1. Amount
2. Date (day and month)
3. Time of day

If ANY detail is missing, ask ONE short question for all missing details at once.

If ALL details are present:
- Accept any date format (DD/MM/YYYY, "2nd feb", "feb 2", etc)
- Automatically calculate day_of_week_0 through day_of_week_6 from the date

Return ONLY valid JSON:
{{
  "transaction_amount": float (positive=income, negative=expense),
  "month": int (1-12),
  "day": int (1-31),
  "day_of_week_0": int (1 if Monday else 0),
  "day_of_week_1": int (1 if Tuesday else 0),
  "day_of_week_2": int (1 if Wednesday else 0),
  "day_of_week_3": int (1 if Thursday else 0),
  "day_of_week_4": int (1 if Friday else 0),
  "day_of_week_5": int (1 if Saturday else 0),
  "day_of_week_6": int (1 if Sunday else 0),
  "time_slice": int (morning 6-11=0, afternoon 12-16=1, evening 17-21=2, night=3)
}}
Return ONLY a question OR valid JSON. No markdown.
"""
    response = safe_generate(prompt)
    return response


def safe_json_parse(text):
    text = (
        text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        return json.loads(text)
    except Exception:
        print("\nJSON Parse Failed:")
        print(text)

        raise


def predict_category(features):
    try:
        response = requests.post(
            API_URL,
            json=features,
            timeout=10
        )

        response.raise_for_status()
        return response.json()["predicted_category"]
    except Exception:
        print("Prediction API failed")
        return "unknown"


def get_insight(user_input, category, amount):
    prompt = f"""
Role: Financial Assistant

Input:
User input: {user_input}
Category: {category}
Amount: {amount}
Rules:
If amount > 0:
Income
If amount < 0:
Expense
Tasks:
If Expense:
Decide if expense is reasonable.
If not → suggest ONE way to save money without reducing quality.

If Income:
Suggest ONE way to increase income.
Give ONE useful financial insight.

Output Rules:
Maximum 2 lines.
Actionable advice only.
"""

    response = safe_generate(prompt)
    return response


def run_agent(user_input):

    print("\nUser Input:")
    print(user_input)

    asked_already = False

    while True:

        result = extract_or_ask(
            user_input,
            asked_already
        )
        clean = result.strip().replace("```json","").replace("```","").strip()
        if not clean.startswith("{"):
            print(f"Agent: {result}")
            follow_up = input("You: ")
            user_input = (
                user_input
                + ". "
                + follow_up
            )

            asked_already = True

        else:
            break

    print("\nAnalysing...")

    features = safe_json_parse(result)

    print("\nExtracted Features:")
    print(json.dumps(features, indent=2))

    category = predict_category(features)

    insight = get_insight(
        user_input,
        category,
        features["transaction_amount"]
    )

    print(f"\nCategory: {category}")
    print(f"Insight: {insight}\n")


if __name__ == "__main__":

    print("Spending Predictor Agent")
    print("Describe your transaction in plain English.")
    print("Type 'quit' to exit.\n")

    while True:

        user_input = input("You: ").strip()

        if user_input.lower() == "quit":
            break

        run_agent(user_input)