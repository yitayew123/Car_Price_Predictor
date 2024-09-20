# Car Price Predictor

## Overview
The Car Price Predictor is a web application that allows users to predict the price of a car based on various inputs such as company, model, year of purchase, fuel type, and kilometers driven. The application utilizes a machine learning model to make accurate price predictions.

## Features
- User-friendly interface for selecting car attributes.
- Real-time price prediction based on user input.
- Responsive design that works on various devices.
- Utilizes Bootstrap for styling and layout.
- Includes data visualization for a better user experience.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Data Processing**: Pandas
- **Machine Learning Model**: Linear Regression (loaded with Pickle)
- **Database**: CSV file for cleaned car data

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/car-price-predictor.git

   ## Usage

    - Select the car company from the dropdown list.
    - Choose the car model from the dynamically populated list based on the selected company.
    - Select the year of purchase, fuel type, and enter the kilometers driven.
    - Click the "Predict Price" button to see the predicted price of the car.
