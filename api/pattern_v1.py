from pattern.en import sentiment
from nltk.tokenize import word_tokenize

def get_sentiment(text):
    tokens = word_tokenize(text)
    positive_words = {}
    negative_words = {}
    neutral_words = {}

    for token in tokens:
        polarity = sentiment(token)[0]
        
        if polarity > 0:
            #positive_words.append((token, polarity))
            positive_words[token]=polarity
        elif polarity < 0:
            negative_words[token]=polarity
        else:
            neutral_words[token]=polarity
    
    sentiment_value = sentiment(text)[0]
    sentiment_label = 'Positive' if sentiment_value > 0 else 'Negative' if sentiment_value < 0 else 'Neutral'
    
    return sentiment_label, positive_words, negative_words, neutral_words ,sentiment_value
