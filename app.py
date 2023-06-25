from flask import Flask, Blueprint ,redirect,url_for,render_template,request
from api.api import api
from flasgger import Swagger
import json
import api.textblob_v1 as textblob
import api.pattern_v1 as pattern
import api.vader_v1 as vader
import api.afinn as afinn
import api.sentiwordnet_v1 as sentiwordnet
import api.senticnet as senticnet




app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(api,url_prefix="/api")


@app.route("/")
def index():
    return render_template('landing.html')


@app.route("/demo",methods=["POST","GET"])
def demo():
    if request.method == 'POST':
        lexicon_model = request.form.get("lexicon")
        text = request.form.get('text')
        if lexicon_model == 'TextBlob':
            sentiment, positive_words, negative_words, neutral_words, compound_score = textblob.get_sentiment(text)
            processed_data = {"sentiment_label":sentiment,"positive_words":positive_words,"negative_words":negative_words,"neutral_words":neutral_words,"sentiment_score":compound_score}
            return render_template("result.html",processed_data=processed_data)
        elif lexicon_model == 'SentiWordNet':
            sentiment, positive_words, negative_words, neutral_words, compound_score = sentiwordnet.get_sentiment(text)
            processed_data ={"sentiment_label":sentiment,"positive_words":positive_words,"negative_words":negative_words,"neutral_words":neutral_words,"sentiment_score":compound_score}
            return render_template("result.html",processed_data=processed_data)
        elif lexicon_model == 'AFINN':
            sentiment, positive_words, negative_words, neutral_words, compound_score = afinn.get_sentiment(text)
            processed_data ={"sentiment_label":sentiment,"positive_words":positive_words,"negative_words":negative_words,"neutral_words":neutral_words,"sentiment_score":compound_score}
            return render_template("result.html",processed_data=processed_data)
        elif lexicon_model == 'VADER':
            sentiment, positive_words, negative_words, neutral_words, compound_score = vader.get_sentiment(text)
            processed_data ={"sentiment_label":sentiment,"positive_words":positive_words,"negative_words":negative_words,"neutral_words":neutral_words,"sentiment_score":compound_score}
            return render_template("result.html",processed_data=processed_data)
        elif lexicon_model == 'Pattern':
            sentiment, positive_words, negative_words, neutral_words, compound_score = pattern.get_sentiment(text)
            processed_data ={"sentiment_label":sentiment,"positive_words":positive_words,"negative_words":negative_words,"neutral_words":neutral_words,"sentiment_score":compound_score}
            return render_template("result.html",processed_data=processed_data)
        elif lexicon_model == 'SenticNet':
            sentiment, positive_words, negative_words, neutral_words, compound_score = senticnet.get_sentiment(text)
            processed_data ={"sentiment_label":sentiment,"positive_words":positive_words,"negative_words":negative_words,"neutral_words":neutral_words,"sentiment_score":compound_score}
            return render_template("result.html",processed_data=processed_data)
            
    else:
        return render_template("demo.html")
    


 
""" if __name__ == "__main__":
    app.run(debug=True) """

