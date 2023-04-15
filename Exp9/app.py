import nltk
import pickle
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from flask import Flask, render_template, request, send_file

nltk.download('stopwords')
vect = pickle.load(open('../vec.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    print(request.form)
    ini_feature = [int(x) for x in request.form.values()]
    print(ini_feature)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
