from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    polarity_score = blob.sentiment.polarity
    sentiment = 'Positive' if polarity_score > 0 else 'Negative' if polarity_score < 0 else 'Neutral'

    positive_words = {}
    negative_words = {}
    neutral_words = {}

    for word in blob.words:
        word_blob = TextBlob(word)
        word_polarity = word_blob.sentiment.polarity
        word_subjectivity = word_blob.sentiment.subjectivity

        if word_polarity > 0:
            #positive_words.append({word:word_polarity})
            positive_words[word]=word_polarity
        elif word_polarity < 0:
            #negative_words.append({word:word_polarity})
            negative_words[word]=word_polarity
        else:
            #neutral_words.append({word:word_polarity})
            neutral_words[word]=word_polarity

    return sentiment, positive_words, negative_words, neutral_words, polarity_score

