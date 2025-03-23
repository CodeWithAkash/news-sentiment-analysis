import streamlit as st
import requests

# Title of the application
st.title("News Summarization and Sentiment Analysis")

# List of companies for the dropdown
companies = [
    "Google", "Apple", "Amazon", "Tesla", "Samsung", "Nvidia", "Groww", 
    "Microsoft", "TCS", "Wipro", "Flipkart", "Nestle", "Boat", "Accenture", "Meta"
]

# Dropdown for company selection
company_name = st.selectbox("Select a Company", companies)

# Button to fetch news
if st.button("Fetch News"):
    if company_name:
        try:
            # Call the backend API to fetch news
            response = requests.get(f"http://localhost:8000/news/{company_name}")
            
            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()
                articles = data['articles']
                sentiment_results = data['sentiment']

                # Display articles
                st.write("### Extracted Articles")
                for article in articles:
                    st.write(f"**Title:** {article['title']}")
                    st.write(f"**Summary:** {article['summary']}")
                    st.write("---")

                # Display sentiment analysis
                st.write("### Sentiment Analysis")
                st.write(f"Positive: {sentiment_results['positive']}")
                st.write(f"Negative: {sentiment_results['negative']}")
                st.write(f"Neutral: {sentiment_results['neutral']}")

                # Generate TTS
                summary = " ".join([article['summary'] for article in articles if article['summary']])
                if summary:  # Ensure summary is not empty
                    try:
                        tts_response = requests.post(
                            "http://localhost:8000/tts/",
                            json={"text": summary}
                        )
                        if tts_response.status_code == 200:
                            audio_file = tts_response.json()['audio_file']
                            st.audio(audio_file)
                        else:
                            st.error("Failed to generate text-to-speech.")
                    except Exception as e:
                        st.error(f"An error occurred while generating TTS: {e}")
                else:
                    st.warning("No summary available for text-to-speech.")
            else:
                st.error(f"Failed to fetch news. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please select a company from the dropdown.")