from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text.
    Returns a polarity score between -1 and 1.
    """
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def get_crypto_news_sentiment(symbol):
    """
    Simulates sentiment analysis for crypto news.
    In a real app, this would fetch from a news API.
    """
    # Mock data for demo
    mock_news = [
        f"{symbol} reaches new all-time high amidst institutional interest.",
        f"Regulatory concerns weigh down {symbol} market sentiment.",
        f"New technology upgrade for {symbol} network promised soon.",
        "Major exchange lists new trading pairs for top cryptocurrencies."
    ]
    
    sentiments = [analyze_sentiment(news) for news in mock_news]
    avg_sentiment = sum(sentiments) / len(sentiments)
    
    return avg_sentiment, mock_news
