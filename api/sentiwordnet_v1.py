from nltk.corpus import sentiwordnet as swn
from nltk.tokenize import word_tokenize

def get_sentiment(text):
    tokens = word_tokenize(text)
    positive_words = {}
    negative_words = {}
    neutral_words = {}

    for token in tokens:
        synsets = list(swn.senti_synsets(token))
        
        if synsets:
            # Get the average positive and negative scores for all synsets of the token
            pos_score = sum(synset.pos_score() for synset in synsets) / len(synsets)
            neg_score = sum(synset.neg_score() for synset in synsets) / len(synsets)
            
            if pos_score > neg_score:
                positive_words[token] = pos_score
            elif neg_score > pos_score:
                negative_words[token] = neg_score
            else:
                neutral_words[token] = pos_score
        else:
            neutral_words[token] = 0
    
    # Calculate overall polarity score
    overall_polarity = (sum(positive_words.values()) - sum(negative_words.values())) / (len(positive_words) + len(negative_words))
    
    sentiment = 'Positive' if len(positive_words) > len(negative_words) else 'Negative' if len(negative_words) > len(positive_words) else 'Neutral'
    
    return sentiment, positive_words, negative_words, neutral_words,overall_polarity
