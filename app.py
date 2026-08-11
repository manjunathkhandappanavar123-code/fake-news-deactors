import streamlit as st
from models_list import detect_fake_news

st.set_page_config(
    page_title="AI Fake News Detector",
    page_icon="📰",
    layout="centered"
)

st.title("📰 AI Fake News Detector")

st.write("Paste any news article or headline below.")

news = st.text_area(
    "Enter News",
    height=220,
    placeholder="Paste any news here..."
)

if st.button("Analyze News", use_container_width=True):

    if news.strip() == "":
        st.warning("Please enter some news.")
    else:

        with st.spinner("Checking News..."):
            result = detect_fake_news(news)

        if result == "YES":
            st.success("✅ YES")
            st.write("This news appears to be **REAL**.")

        elif result == "NO":
            st.error("❌ NO")
            st.write("This news appears to be **FAKE**.")

        else:
            st.warning(result)