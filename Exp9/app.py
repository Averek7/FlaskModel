import re
import pandas as pd
from textblob import TextBlob
from flask import Flask, render_template, request, send_file

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analysis', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        uploaded_file = request.files['file']

        if not uploaded_file:
            return render_template('index.html', error_message='Please upload a file')

        try:
            tweets = pd.read_csv(uploaded_file, encoding="ISO-8859-1")
        except:
            return render_template('index.html', error_message='Invalid file format. Please upload a CSV file')

        def CleanTxt(text):
            text = re.sub(r'@[A-Za-z0-9]+', '', text)
            text = re.sub(r'#', '', text)
            text = re.sub(r'RT[\s]+', '', text)
            text = re.sub(r'https?:\/\/\S+', '', text)
            return text

        tweets['Tweet'] = tweets['Tweet'].apply(CleanTxt)

        def getSubjectivity(text):
            return TextBlob(text).sentiment.subjectivity

        def getPolarity(text):
            return TextBlob(text).sentiment.polarity

        tweets['Subjectivity'] = tweets['Tweet'].apply(getSubjectivity)
        tweets['Polarity'] = tweets['Tweet'].apply(getPolarity)

        def getAnalysis(score):
            if (score < 0):
                return 'Negative'
            elif (score == 0):
                return 'Neutral'
            else:
                return 'Positive'

        tweets['Analysis'] = tweets['Polarity'].apply(getAnalysis)

        tweets.to_csv('analysis.csv', index=False)

        return send_file('analysis.csv', as_attachment=True)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
