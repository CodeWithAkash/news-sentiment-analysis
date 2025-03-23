from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# News API Configuration
NEWS_API_KEY = "c0bdf992b01842188769ab55655d4f2f" 
NEWS_API_URL = "https://web-production-c7453.up.railway.app/get_news"

@app.route("/get_news", methods=["GET"])
def get_news():
    company = request.args.get("q", "Tesla")
    params = {
        "q": company,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "publishedAt"
    }
    
    response = requests.get(NEWS_API_URL, params=params)
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Unable to fetch news"}), 500

if __name__ == "__main__":
    app.run(debug=True)
