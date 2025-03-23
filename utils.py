from textblob import TextBlob
from gtts import gTTS

def analyze_sentiment(text):
    return "Positive" if TextBlob(text).sentiment.polarity > 0 else "Negative" if TextBlob(text).sentiment.polarity < 0 else "Neutral"

def text_to_speech(text, filename="news_audio.mp3"):
    if text.strip():
        gTTS(text=text, lang="hi", slow=False).save(filename)
        return filename
    return None
