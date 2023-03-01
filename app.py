import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open('./model.pkl', 'rb'))


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
    ini_feature = [int(x) for x in request.form.values()]
    final_features = [np.array(ini_feature)]
    pred = model.predict(final_features)

    output = round(pred[0], 2)

    # return render_template('index.html', prediction_text=)
    return "Salary for YOE should be ${}".format(output)


if __name__ == "__main__":
    app.run(debug=True)
