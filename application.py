# Import necessary libraries and modules
from flask import Flask, render_template, \
    request  # Flask for web app, render_template to render HTML, request to handle form data
import pandas as pd  # For data handling and analysis
import pickle  # To load the trained machine learning model
import numpy as np  # For numerical operations like rounding

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained linear regression model using pickle
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

# Load the cleaned car dataset into a DataFrame
car = pd.read_csv('Cleaned_Car_data.csv')


# Define the route for the home page
@app.route('/')
def index():
    # Get unique values for car companies, models, years, and fuel types from the dataset
    companies = sorted(car['company'].unique())  # Sort and get unique car companies
    car_models = sorted(car['name'].unique())  # Sort and get unique car models
    year = sorted(car['year'].unique(), reverse=True)  # Get unique years in descending order
    fuel_type = car['fuel_type'].unique()  # Get unique fuel types

    # Add a default option to select a company at the beginning of the list
    companies.insert(0, 'Select Company')

    # Render the index.html template and pass the variables for companies, car models, years, and fuel types
    return render_template('index.html', companies=companies, car_models=car_models, years=year, fuel_types=fuel_type)


# Define the route for handling predictions via POST request
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data submitted by the user
    company = request.form.get('company')  # Get the selected car company from the form
    car_model = request.form.get('car_models')  # Get the selected car model from the form
    year = request.form.get('year')  # Get the selected manufacturing year from the form
    fuel_type = request.form.get('fuel_type')  # Get the selected fuel type from the form
    kms_driven = request.form.get('kilo_driven')  # Get the input for kilometers driven from the form

    # Make a prediction using the trained model by passing input data as a DataFrame
    prediction = model.predict(pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]],
                                            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']))

    # Return the predicted car price, rounded to 2 decimal places, as a string
    return str(np.round(prediction[0], 2))


# Run the Flask application in debug mode if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
