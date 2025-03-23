import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from gtts import gTTS

# Function to scrape news articles from Google News
def scrape_news(company_name):
    try:
        url = f"https://news.google.com/search?q={company_name}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = []

        for item in soup.find_all('article')[:10]:  # Limit to 10 articles
            try:
                title = item.find('a', class_='DY5T1d').text
                link = "https://news.google.com" + item.find('a', class_='DY5T1d')['href']
                summary = item.find('div', class_='Da10Tb').text if item.find('div', class_='Da10Tb') else "No summary available"
                articles.append({
                    'title': title,
                    'link': link,
                    'summary': summary
                })
            except AttributeError:
                # Skip articles with missing data
                continue
        
        # Log the fetched articles
        print("Fetched articles:")
        for article in articles:
            print(f"Title: {article['title']}")
            print(f"Summary: {article['summary']}")
            print("---")
        
        return articles
    except Exception as e:
        raise Exception(f"Failed to scrape news: {e}")

# Function to perform sentiment analysis
def analyze_sentiment(text):
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)[0]
    return result['label'], result['score']

# Function to compare sentiments across articles
def compare_sentiments(articles):
    sentiments = [analyze_sentiment(article['summary'])[0] for article in articles]
    positive = sentiments.count('POSITIVE')
    negative = sentiments.count('NEGATIVE')
    neutral = sentiments.count('NEUTRAL')
    return {
        'positive': positive,
        'negative': negative,
        'neutral': neutral
    }

# Function to convert text to Hindi speech
def text_to_speech(text, language='hi'):
    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")
    return "output.mp3"