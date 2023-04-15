import pickle
import nltk
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('stopwords')

tweets = pd.read_csv(
    'F:\\6th Sem\\ML\\Assignment\\flaskmodel\\tweets.csv', encoding="latin1")

tweets.drop(['Unnamed: 0', 'Time', 'User'], axis=1, inplace=True)

tweets['clean'] = tweets['Tweet'].apply(lambda x: ' '.join(
    [word for word in x.split() if word.lower() not in set(stopwords.words('english'))]))

count_vectorizer = CountVectorizer()
count = count_vectorizer.fit_transform(tweets['Tweet'])


Y = tweets['Tweet']

arr = tweets.values
label = np.delete(arr, [1], axis=1)
label = label.ravel()

x_train, x_test, y_train, y_test = train_test_split(
    count, label, test_size=0.2, random_state=42)
l_count = LogisticRegression()
l_count.fit(x_train, y_train)

# Saving model to disk
pickle.dump(l_count, open('model.pkl', 'wb'))
pickle.dump(count_vectorizer, open('vec.pkl', 'wb'))

print(tweets)
