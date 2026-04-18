import streamlit as st
import json
from agent import safe_generate, safe_json_parse, predict_category, get_insight

st.set_page_config(
    page_title="Spending Predictor",
    page_icon="💸",
    layout="centered"
)


st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;600&display=swap');

/* Force dark background everywhere */
html, body, [class*="css"], .stApp, .main, section.main {
    font-family: 'DM Sans', sans-serif;
    background-color: #0f0f0f !important;
    color: #f5f5f5 !important;
}

.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    max-width: 600px;
    background-color: #0f0f0f !important;
}

.title {
    font-family: 'DM Serif Display', serif;
    font-size: 3rem;
    text-align: center;
    background: linear-gradient(90deg, #c8f04d, #8cffb5);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}

.subtitle {
    text-align: center;
    color: #aaaaaa !important;
    font-size: 1rem;
    margin-bottom: 2rem;
}

/* Input box - visible text and cursor */
.stTextInput > div > div > input {
    background-color: #1e1e1e !important;
    color: #f5f5f5 !important;
    caret-color: #c8f04d !important;
    border: 1px solid #3a3a3a !important;
    border-radius: 10px !important;
    padding: 0.9rem 1rem !important;
    font-size: 0.95rem !important;
}

.stTextInput > div > div > input::placeholder {
    color: #666666 !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(90deg, #c8f04d, #8cffb5) !important;
    color: #000 !important;
    font-weight: 600 !important;
    border-radius: 10px !important;
    padding: 0.7rem 2rem !important;
    width: 100%;
    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 18px rgba(200,240,77,0.25);
}

/* Result card */
.result-box {
    background: #1a1a1a !important;
    border: 1px solid #2a2a2a;
    border-radius: 16px;
    padding: 1.8rem 2rem;
    margin-top: 2rem;
    box-shadow: 0 10px 35px rgba(0,0,0,0.5);
}

.category-label, .insight-label {
    font-size: 0.7rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #aaaaaa !important;
    margin-bottom: 0.3rem;
}

.category-value {
    font-family: 'DM Serif Display', serif;
    font-size: 2.3rem;
    color: #c8f04d;
    margin-bottom: 1.5rem;
}

.insight-value {
    font-size: 1rem;
    color: #dddddd !important;
    line-height: 1.7;
}

.divider {
    border: none;
    border-top: 1px solid #2a2a2a;
    margin: 1.2rem 0;
}

/* Warning and error text visibility */
.stWarning, .stError {
    color: #f5f5f5 !important;
}

</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="title">💸 Spending Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Describe a transaction in plain English and get instant categorization with insight.</div>',
    unsafe_allow_html=True
)



user_input = st.text_input(
    "",
    placeholder="e.g. I spent ₹450 on dinner last Friday night"
)


if st.button("Analyse Transaction"):

    if not user_input.strip():
        st.warning("Please enter a transaction description.")

    else:

        with st.spinner("Analysing transaction..."):

            try:

                result = safe_generate(f"""
A user described a transaction:
"{user_input}"

Make reasonable assumptions for any missing details.
Accept any date format.
Automatically calculate day_of_week_0 through day_of_week_6 from the date.

Return ONLY valid JSON with these exact keys:
{{
  "transaction_amount": float,
  "month": int,
  "day": int,
  "day_of_week_0": int,
  "day_of_week_1": int,
  "day_of_week_2": int,
  "day_of_week_3": int,
  "day_of_week_4": int,
  "day_of_week_5": int,
  "day_of_week_6": int,
  "time_slice": int
}}
Return ONLY JSON.
""")

                features = safe_json_parse(result)

                category = predict_category(features)

                insight = get_insight(
                    user_input,
                    category,
                    features["transaction_amount"]
                )

                st.markdown(f"""
<div class="result-box">

<div class="category-label">
Predicted Category
</div>

<div class="category-value">
{category}
</div>

<hr class="divider">

<div class="insight-label">
Financial Insight
</div>

<div class="insight-value">
{insight}
</div>

</div>
""", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")