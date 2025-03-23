from textblob import TextBlob
from gtts import gTTS
import os

# Sentiment Analysis Function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"

# Text-to-Speech Function (Hindi)
def text_to_speech(text, filename="news_audio.mp3"):
    try:
        tts = gTTS(text=text, lang="hi")
        tts.save(filename)
        return filename
    except Exception as e:
        print(f"Error in Text-to-Speech: {e}")
        return None
