import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

diabetes = pd.read_csv('diabetes.csv')

features = ['BloodPressure', 'BMI', 'Age']
target = 'Outcome'

x = diabetes[features]
y = diabetes[target]

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42)

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)


pickle.dump(log_reg, open('model2.pkl', 'wb'))

model = pickle.load(open('model2.pkl', 'rb'))

print(model)
