# app/main.py

from pathlib import Path
import streamlit as st
import joblib

#Model and Vecrorizer Path
BASE_DIR = Path(__file__).resolve().parent.parent
VECTORIZER_PATH = BASE_DIR / "tfidf_vectorizer.pkl"
MODEL_PATH = BASE_DIR / "svm_model.pkl"

vectorizer = joblib.load(VECTORIZER_PATH)
model = joblib.load(MODEL_PATH)

# App UI
# Add a background image

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.pcworld.com/wp-content/uploads/2026/01/shutterstock_2495795811-2.jpg?quality=50&strip=all");
        background-size: cover;
        background-opacity: 0.4;
        background-position: top center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Add a Title and Description
st.set_page_config(page_title="SMS Spam Classifier", layout="centered")

st.markdown(
    "<h1 style='color: darkblue; text-align: center;'>📩 SMS Spam Detection System</h1>",
    unsafe_allow_html=True,
)

st.markdown("Enter a message below to check if it's spam or not.")
# Text input
user_input = st.text_area("Enter SMS Text Here:")

# Predict Spam or Not
if st.button("🔍Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message to classify.")
    else:
        # Transform input
        transformed_input = vectorizer.transform([user_input])
        prediction = model.predict(transformed_input)[0]
        
        # Display result
        if prediction == "spam":
            st.error("This message is SPAM! Please be cautious and avoid clicking on any links or providing personal information.")
        else:
            st.success("This message is NOT SPAM and is safe to read.")