import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


diabetes = pd.read_csv('./diabetes.csv')


features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
target = 'Outcome'

# Split the data into features and target variable
x = diabetes[features]
y = diabetes[target]

from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression()
log_reg.fit(x, y)


pregnancies = int(input('Enter number of pregnancies: '))
glucose = int(input('Enter glucose level: '))
bloodPressure = int(input('Enter blood pressure: '))
skinThickness = int(input('Enter skin thickness: '))
insulin = int(input('Enter insulin level: '))
bmi = float(input('Enter BMI: '))
dpf = float(input('Enter diabetes pedigree function: '))
age = int(input('Enter age: '))


input = [[pregnancies, glucose, bloodPressure, skinThickness, insulin, bmi, dpf, age]]
prediction = log_reg.predict(input)


if prediction[0] == 0:
    print('=> The person is not likely to have diabetes :)')
else:
    print('=> The person is likely to have diabetes :(')
