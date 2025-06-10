import streamlit as st
from transformers import pipeline

# Initialize summarizer


# Streamlit App UI
st.set_page_config(page_title="Text Summarizer", layout="centered")
st.title("🧠 AI-Powered Text Summarizer")
st.write("Paste your long text below and get a summary using a transformer model.")

# Text Input
user_input = st.text_area("✍️ Enter your text here:", height=300)

# Summary Button
if st.button("Summarize"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Summarizing..."):
            summary = "Check Summary"
            st.success("✅ Summary:")
            st.write(summary)
