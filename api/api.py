from flask import Blueprint,jsonify, request
from flasgger import Swagger
from flasgger import swag_from
import api.textblob_v1 as textblob
import api.pattern_v1 as pattern
import api.vader_v1 as vader
import api.afinn as afinn
import api.sentiwordnet_v1 as sentiwordnet
import api.senticnet as senticnet


api = Blueprint("api", __name__,static_folder="",template_folder="")


@api.post('/TextBlob')
def TextBlob():
    """
    A simple endpoint to sentiment using TextBlob with a POST request.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            text:
              type: string
              description: The Text for which you need to Find the Sentimaent.
    responses:
      200:
        description: A greeting message.
    """
    data = request.get_json()
    name = data['text']
    sentiment, positive_words, negative_words, neutral_words, compound_score = textblob.get_sentiment(name)
    return jsonify({"sentiment_label":sentiment,"positive_words":positive_words,"negative_words":negative_words,"neutral_words":neutral_words,"sentiment_score":compound_score})


@api.post('/Pattern')
def Pattern():
    """
    A simple endpoint to sentiment using Pattern with a POST request.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            text:
              type: string
              description: The Text for which you need to Find the Sentimaent.
    responses:
      200:
        description: A greeting message.
    """
    data = request.get_json()
    name = data['text']
    sentiment, positive_words, negative_words, neutral_words, compound_score = pattern.get_sentiment(name)
    return jsonify({"sentiment_label":sentiment,"positive_words":positive_words,"negative_words":negative_words,"neutral_words":neutral_words,"sentiment_score":compound_score})


@api.post('/Vader')
def Vader():
    """
    A simple endpoint to sentiment using Vader with a POST request.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            text:
              type: string
              description: The Text for which you need to Find the Sentimaent.
    responses:
      200:
        description: A greeting message.
    """
    data = request.get_json()
    name = data['text']
    sentiment, positive_words, negative_words, neutral_words, compound_score = vader.get_sentiment(name)
    return jsonify({"sentiment_label":sentiment,"positive_words":positive_words,"negative_words":negative_words,"neutral_words":neutral_words,"sentiment_score":compound_score})

@api.post('/SentiWordNet')
def SentiWordNet():
    """
    A simple endpoint to sentiment using SentiWordNet with a POST request.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            text:
              type: string
              description: The Text for which you need to Find the Sentimaent.
    responses:
      200:
        description: A greeting message.
    """
    data = request.get_json()
    name = data['text']
    sentiment, positive_words, negative_words, neutral_words, compound_score = sentiwordnet.get_sentiment(name)
    return jsonify({"sentiment_label":sentiment,"positive_words":positive_words,"negative_words":negative_words,"neutral_words":neutral_words,"sentiment_score":compound_score})


@api.post('/Senticnet')
def Senticnet():
    """
    A simple endpoint to sentiment using Senticnet with a POST request.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            text:
              type: string
              description: The Text for which you need to Find the Sentimaent.
    responses:
      200:
        description: A greeting message.
    """
    data = request.get_json()
    name = data['text']
    sentiment, positive_words, negative_words, neutral_words, compound_score = senticnet.get_sentiment(name)
    return jsonify({"sentiment_label":sentiment,"positive_words":positive_words,"negative_words":negative_words,"neutral_words":neutral_words,"sentiment_score":compound_score})


@api.post('/AFINN')
def afinn():
    """
    A simple endpoint to sentiment using Senticnet with a POST request.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            text:
              type: string
              description: The Text for which you need to Find the Sentimaent.
    responses:
      200:
        description: A greeting message.
    """
    data = request.get_json()
    name = data['text']
    sentiment, positive_words, negative_words, neutral_words, compound_score = afinn.get_sentiment(name)
    return jsonify({"sentiment_label":sentiment,"positive_words":positive_words,"negative_words":negative_words,"neutral_words":neutral_words,"sentiment_score":compound_score})
