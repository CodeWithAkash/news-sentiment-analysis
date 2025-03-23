---
title: "News Sentiment Analysis App"
emoji: "📰"
colorFrom: "blue"
colorTo: "green"
sdk: "streamlit"
sdk_version: "1.25.0"
app_file: "app.py"
pinned: false
---

# News Sentiment Analysis App

A web-based application that fetches news articles for a selected company, analyzes sentiment, and provides a Hindi text-to-speech (TTS) summary.

## Features
- Fetches news articles using an API
- Performs sentiment analysis on news headlines & descriptions
- Generates Hindi audio summaries using text-to-speech (gTTS)
- Built with Streamlit (Frontend) & Flask (Backend API)

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/news-sentiment-analysis.git
cd news-sentiment-analysis
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Run the Flask API (Backend)
```sh
python api.py
```
API Endpoint: `http://127.0.0.1:5000/get_news?company=your_selected_company`

### 4. Run the Streamlit App (Frontend)
```sh
streamlit run app.py
```
App URL: `http://localhost:8501/`

## API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| `GET` | `/get_news?company=your_selected_company` | Fetch news articles for a selected company |
| `POST` | `/analyze_sentiment` | Analyze sentiment of a text |
| `POST` | `/generate_audio` | Convert text to Hindi audio |

## Contributing
Feel free to fork and submit a pull request.

## License
This project is licensed under the MIT License.

