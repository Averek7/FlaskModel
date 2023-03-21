import pandas as pd
import pickle
import warnings
from sklearn.linear_model import LinearRegression

warnings.filterwarnings("ignore", category=DeprecationWarning)

data = pd.read_csv('flaskmodel/Salary_Data.csv')

feature = ['YearsExperience']
target = 'Salary'
x = data[feature]
y = data[target]

LReg = LinearRegression()
LReg.fit(x, y)

pickle.dump(LReg, open('model.pkl', 'wb'))

model = pickle.load(open('model.pkl', 'rb'))

print(model)
