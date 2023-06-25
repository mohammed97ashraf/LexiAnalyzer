from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

def get_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    tokens = word_tokenize(text)
    over_all_score = 0
    positive_words = {}
    negative_words = {}
    neutral_words = {}

    for token in tokens:
        sentiment_scores = sid.polarity_scores(token)
        compound_score = sentiment_scores['compound']
        
        if compound_score >= 0.5:
            over_all_score = over_all_score+compound_score
            positive_words[token]=compound_score
        elif compound_score <= -0.5:
            over_all_score = over_all_score+compound_score
            negative_words[token]=compound_score
        else:
            neutral_words[token]=compound_score
    
    sentiment = 'Positive' if len(positive_words) > len(negative_words) else 'Negative' if len(negative_words) > len(positive_words) else 'Neutral'
    return sentiment, positive_words, negative_words, neutral_words, over_all_score
