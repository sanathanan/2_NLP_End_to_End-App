from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap

# NLP Libraries
from textblob import TextBlob, Word
import random

import time

# Giving our app name as "app"
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyse', methods=['POST'])
def analyse():
    start = time.time()
    if request.method == 'POST':
        user_input_text = request.form['rawtext']
        # NLP
        blob = TextBlob(user_input_text ) # passing my text from the user input to blob
        received_text1 = blob

        # We need to find the sentiment and subjectivity of the text
        blob_sentiment, blob_subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity

        # we are breaking down the text into words
        number_of_tokens = list(blob.words)
        number_of_tokens = len(number_of_tokens)

        nouns = list()
        for word, tag in blob.tags:
            if tag == 'NN':
                nouns.append(word.lemmatize())
                len_of_words = len(nouns)
                rand_words = random.sample(nouns, len(nouns))
                final_word = list()
                for item in rand_words:
                    word = Word(item).pluralize()
                    final_word.append(word)
                    summary = final_word
                    end = time.time()
                    final_time = end - start

    return render_template('index.html',
                           received_text = received_text1,
                           blob_sentiment = blob_sentiment,
                           blob_subjectivity = blob_subjectivity,
                           number_of_tokens = number_of_tokens,
                           summary=summary,
                           final_time=final_time
                           )

# Running the file
if __name__ == '__main__':
    app.run(debug=True)
