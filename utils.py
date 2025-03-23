from textblob import TextBlob
from gtts import gTTS
from googletrans import Translator
import os

# Sentiment Analysis Function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"

# Function to Translate Text to Hindi
def translate_to_hindi(text):
    translator = Translator()
    translated_text = translator.translate(text, src="en", dest="hi").text
    return translated_text

# Text-to-Speech Function (Hindi)
def text_to_speech(text, filename="news_audio.mp3"):
    try:
        text = text.strip()
        if not text:
            return None

        print(f"🔊 Translating and converting to Hindi Speech: {text}")

        # Translate text to Hindi before TTS
        hindi_text = translate_to_hindi(text)
        print(f"✅ Translated Text: {hindi_text}")

        # Generate Hindi TTS
        tts = gTTS(text=hindi_text, lang="hi", slow=False)
        tts.save(filename)
        return filename
    except Exception as e:
        print(f"❌ Error in Text-to-Speech: {e}")
        return None