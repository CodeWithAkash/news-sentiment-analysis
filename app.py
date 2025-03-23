import streamlit as st
import requests
from utils import analyze_sentiment, text_to_speech

# API Endpoint
API_URL = "https://news-sentiment-analysis-faw9.onrender.com/get_news"

# Predefined list of companies
companies = ["Tesla","Accenture", "Apple", "Google", "Amazon", "Microsoft", "Meta", "TCS","Flipkart", "Facebook", "Meta", "Wipro", "Uber", "Jio", "Airtel"]
st.title("📰 News Sentiment Analysis App")

# Drop-down for company selection
company = st.selectbox("Select a Company:", companies)

# Initialize session state for articles
if "articles" not in st.session_state:
    st.session_state.articles = []

if st.button("Fetch & Analyze News"):
    params = {"q": company}
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        st.session_state.articles = response.json().get("articles", [])

        if st.session_state.articles:
            for article in st.session_state.articles[:2]:  # Show first 5 articles
                title = article.get("title", "No Title")
                description = article.get("description", "No Description")
                sentiment = analyze_sentiment(title + " " + description)

                st.subheader(title)
                st.write(description)
                st.write(f"**Sentiment:** {sentiment}")
                st.write(f"📅 {article.get('publishedAt', 'N/A')} | 🏛 {article.get('source', {}).get('name', 'Unknown')}")
                st.markdown(f"[🔗 Read More]({article.get('url')})")
                st.write("---")
        else:
            st.write("⚠ No news found. Try another company.")
    else:
        st.write("❌ Error fetching news.")

# Generate Hindi audio summary
if st.button("Generate Hindi Audio Summary"):
    if st.session_state.articles:
        text_summary = " ".join([article["title"] for article in st.session_state.articles[:2]])
        audio_file = text_to_speech(text_summary)
        st.audio(audio_file, format="audio/mp3")
    else:
        st.write("⚠ No articles available. Fetch news first.")
