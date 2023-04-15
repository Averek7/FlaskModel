from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string
import nltk
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
import pickle


df = pd.read_csv("../spam.csv", encoding="latin1")

df.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)

df.rename(columns={'v1': 'target', 'v2': 'text'}, inplace=True)

encoder = LabelEncoder()

df['target'] = encoder.fit_transform(df['target'])

df = df.drop_duplicates(keep='first')

nltk.download('stopwords')
nltk.download('punkt')
ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


df['transformed_text'] = df['text'].apply(transform_text)

cv = CountVectorizer()
tfidf = TfidfVectorizer(max_features=3000)


X = tfidf.fit_transform(df['transformed_text']).toarray()

y = df['target'].values


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=2)


mnb = MultinomialNB()

mnb.fit(X_train, y_train)
y_pred2 = mnb.predict(X_test)
print(accuracy_score(y_test, y_pred2))

pickle.dump(tfidf, open('vectorizer.pkl', 'wb'))
pickle.dump(mnb, open('model3.pkl', 'wb'))
