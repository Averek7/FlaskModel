# Machine Learning 
=> Lab assignment - 7,8 and 9

# By UI20CS04 and UI20CS12
🕴 Alok Kumar and Avanish Singh

# To run the model 

`flask run`

# Lab 7

`Language - Python and flask`

To embed a developed machine learning model into a web page for logistic regression using Python and Flask, we would need to follow these steps:
1. Train our logistic regression model using Python, and save the model as a file. We can use libraries such as scikit-learn to build and train our model.
2. Create a Flask web application that will serve as the interface for your model. This can be done using Python, and Flask, which is a lightweight web framework for Python.
3. Define an API endpoint in Flask that will receive input data for the logistic regression model. This endpoint should accept input data in a JSON format.
4. Load the trained logistic regression model file in your Flask application.
5. Use the Flask endpoint to pass the input data to the model and get the predicted output.
6. Embed the model prediction into your web page using HTML, CSS, and JavaScript.
7. Deploy your Flask web application to a web server so that it can be accessed from anywhere.

With these steps, we have embed a developed machine learning model into a web page for logistic regression using Python and Flask.

# Lab - 8

`Language - Python and flask`

To deploy a machine learning model on a web interface using Python and Flask, where users can test their data, follow these steps:
1. Build and train our machine learning model using Python, and save the trained model to a file. We can use libraries such as scikit-learn or TensorFlow to build and train your model.
2. Create a Flask web application using Python, which will serve as the interface for our machine learning model.
3. Define an API endpoint in Flask that will receive input data from the user. If the user is testing a single data item, the endpoint should accept input data in a JSON format. If the user has multiple data items, you can allow them to upload a file in CSV or Zip format. You can use the Flask request module to handle the input data.
4. Load the trained machine learning model file into your Flask application using libraries such as pickle or joblib.
5. Use the Flask endpoint to pass the input data to the model and get the predicted output. You can use the predict method of the trained model to get the output.
6. Display the predicted output on the web page using HTML, CSS, and JavaScript. You can use a template engine such as Jinja2 to render the predicted output in the web page.
7. If the user is testing multiple data items, we can allow them to upload a CSV or Zip file, and use the pandas library in Python to read the data file and pass it to the model for prediction.
8. Deploy your Flask web application to a web server so that it can be accessed by users from anywhere.

With these steps, we can deploy a machine learning model on a web interface using Python and Flask, where users can test their data by either testing a single data item or uploading a file with multiple data items.

# Lab - 9

`Language - Python and flask`

To deploy a machine learning model on the web for real-time sentiment analysis of Twitter data using Python and Flask, follow these steps:

1. Collect Twitter data in real-time using a Twitter API or a web scraping tool like Beautiful Soup.
2. Preprocess the collected Twitter data by removing irrelevant information such as URLs, hashtags, and user mentions. We can also perform text cleaning techniques such as removing stop words, converting all text to lowercase, and stemming.
3. Train a machine learning model for sentiment analysis using Python. We can use libraries like NLTK, Scikit-learn, or TensorFlow to build your model.
4. Save the trained machine learning model to a file.
5. Create a Flask web application that will serve as the interface for our model. This can be done using Python and Flask.
6. Define an API endpoint in Flask that will receive real-time Twitter data for sentiment analysis.
7. Load the trained machine learning model file in your Flask application.
8. Use the Flask endpoint to pass the real-time Twitter data to the model and get the predicted sentiment (positive, negative, or neutral).
9. Display the predicted sentiment on the web page using HTML, CSS, and JavaScript.
10. Deploy your Flask web application to a web server so that it can be accessed by users from anywhere.

With these steps, we can deploy a machine learning model on the web for real-time sentiment analysis of Twitter data using Python and Flask.
