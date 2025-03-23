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
        # Ensure text is properly encoded
        text = text.strip()
        if not text:
            return None

        print(f"🔊 Converting to Hindi Speech: {text}")

        # Generate Hindi TTS
        tts = gTTS(text=text, lang="hi", slow=False)
        tts.save(filename)
        return filename
    except Exception as e:
        print(f"❌ Error in Text-to-Speech: {e}")
        return None
