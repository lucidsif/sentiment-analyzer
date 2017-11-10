from flask import Flask, redirect, render_template, request, url_for

import helpers
from analyzer import Analyzer
import os
import sys

positives = os.path.join(sys.path[0], "positive-words.txt")
negatives = os.path.join(sys.path[0], "negative-words.txt")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))
    
    positive_total = 0
    negative_total = 0
    neutral_total = 0

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)
    
    if tweets == None:
        return redirect(url_for("index"))
    
    # for each tweet
    for tweet in tweets:
        analyzer = Analyzer(positives, negatives)
        score = analyzer.analyze(tweet)
        if (score > 0.0):
            positive_total += 1
        elif (score < 0.0):
            negative_total += 1
        else:
            neutral_total += 1

    # generate chart
    chart = helpers.chart(positive_total, negative_total, neutral_total)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
