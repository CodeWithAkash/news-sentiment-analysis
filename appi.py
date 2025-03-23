from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import scrape_news, analyze_sentiment, compare_sentiments, text_to_speech

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Endpoint to fetch news and sentiment analysis
@app.route('/news/<company_name>', methods=['GET'])
def get_news(company_name):
    try:
        # Fetch news articles for the given company
        articles = scrape_news(company_name)
        
        # Perform sentiment analysis on the articles
        sentiment_results = compare_sentiments(articles)
        
        # Return the articles and sentiment analysis results
        return jsonify({
            "articles": articles,
            "sentiment": sentiment_results
        })
    except Exception as e:
        # Handle errors and return a 500 status code
        print(f"Error in get_news: {e}")
        return jsonify({"error": str(e)}), 500

# Endpoint to generate text-to-speech
@app.route('/tts/', methods=['POST'])
def generate_tts():
    try:
        # Get the text from the request
        data = request.json
        text = data.get('text')
        
        # Check if text is provided
        if not text:
            return jsonify({"error": "Text is required"}), 400
        
        # Generate the text-to-speech audio file
        audio_file = text_to_speech(text)
        
        # Return the path to the audio file
        return jsonify({"audio_file": audio_file})
    except Exception as e:
        # Handle errors and return a 500 status code
        print(f"Error in generate_tts: {e}")
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)