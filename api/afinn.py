from afinn import Afinn
import nltk
from nltk.tokenize import word_tokenize

# Load the AFINN wordlist
afinn = Afinn()

def get_sentiment(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Initialize sentiment scores and lists for positive, negative, and neutral words
    sentiment_score = 0
    positive_words = {}
    negative_words = {}
    neutral_words = {}
    
    for token in tokens:
        score = afinn.score(token)
        sentiment_score += score
        
        if score > 0:
            positive_words[token]=score
        elif score < 0:
            negative_words[token]=score
        else:
            neutral_words[token]=score
    
    # Determine overall sentiment
    if sentiment_score > 0:
        sentiment = 'Positive'
    elif sentiment_score < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    # Calculate overall polarity
    overall_polarity = sentiment_score / len(tokens)
    
    return sentiment, positive_words, negative_words, neutral_words, overall_polarity
