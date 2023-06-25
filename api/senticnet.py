import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



df = pd.read_csv('api/senticnet_file.csv')
concept, polarity = list(df['CONCEPT']),list(df['POLARITY INTENSITY'])
senticnet = result_dict = dict(zip(concept, polarity))


def classify_sentiment(word):
    if word in senticnet:
        polarity = senticnet[word]
        if polarity > 0:
            return 'Positive', polarity
        elif polarity < 0:
            return 'Negative', polarity
    return 'Neutral', 0

def get_sentiment(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Initialize sentiment scores
    sentiment_scores = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
    positive_words = {}
    negative_words = {}
    neutral_words = {}
    
    for token in filtered_tokens:
        sentiment, polarity = classify_sentiment(token)
        sentiment_scores[sentiment] += 1
        
        if sentiment == 'Positive':
            positive_words[token]=polarity
        elif sentiment == 'Negative':
            negative_words[token]=polarity
        else:
            neutral_words[token]=polarity
    
    # Determine overall sentiment
    if sentiment_scores['Positive'] > sentiment_scores['Negative']:
        sentiment = 'Positive'
    elif sentiment_scores['Positive'] < sentiment_scores['Negative']:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment, positive_words, negative_words, neutral_words, sentiment_scores