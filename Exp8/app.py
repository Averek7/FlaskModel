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
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        uploaded_file = request.files['file']

        if not uploaded_file:
            return render_template('home.html', error_message='Please upload a file')

        try:
            spam = pd.read_csv(uploaded_file, encoding="ISO-8859-1")
        except:
            return render_template('home.html', error_message='Invalid file format. Please upload a CSV file')

        spam['clean'] = spam['v2'].apply(lambda x: ' '.join(
            [word for word in x.split() if word.lower() not in set(stopwords.words('english'))]))

        count = vect.transform(spam['clean'])

        model = pickle.load(open('../model.pkl', 'rb'))

        predictions = model.predict(count)

        spam['Prediction'] = predictions

        spam.to_csv('predictions.csv', index=False)

        return send_file('predictions.csv', as_attachment=True)

    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
