import os

import pandas as pd
import numpy as np

from flask import Flask, jsonify, render_template, jsonify, request, url_for, json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/red_wine_data")
def red_wine_data():
    return render_template("Wine_Data_Red.html")

@app.route("/white_wine_data")
def white_wine_data():
    return render_template("Wine_Data_White.html")

@app.route("/about")
def about():
    return render_template("About.html")

@app.route("/predictions")
def predictions():
    return render_template("Predictions_Page.html")

@app.route("/visualizations")
def visualizations():
    return render_template("Visualizations.html")

@app.route("/recommendations")
def recommendations():
    return render_template("Recommendations.html")

if __name__ == "__main__":
    app.run()
