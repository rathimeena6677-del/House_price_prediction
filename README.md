🏠 House Price Prediction using Machine Learning

A Machine Learning–powered web application that predicts house prices based on property features such as area, number of bedrooms, and number of bathrooms. Built with Python and Streamlit, the app provides a fast, interactive interface for real-time price estimation.

🔗 Live Demo: https://housepriceprediction-r2zmdsdzaarz8kmjs8qyrv.streamlit.app/


📌 Overview

This project demonstrates an end-to-end Machine Learning workflow — from data preprocessing and model training to serialization and deployment. It uses a Polynomial Regression model to estimate house prices based on key property attributes, wrapped in a clean, user-friendly Streamlit interface.


🎯 Objective

To build a predictive model that estimates house prices using historical housing data, showcasing the complete ML lifecycle: data preprocessing, model training, evaluation, serialization, and deployment as a live web application.


✨ Features


🔮 Predicts house prices based on user-provided inputs
💻 Interactive, easy-to-use web interface built with Streamlit
📈 Machine Learning model trained using Polynomial Regression
⚡ Real-time, fast predictions
🚀 Deployed and publicly accessible via Streamlit Community Cloud

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

📂 Project Structure

textHouse_Price_Prediction/
├── app.py                 # Streamlit application
├── model_pickle           # Serialized trained ML model
├── house_price_data.csv   # Dataset used for training
├── requirements.txt       # Project dependencies
└── README.md               # Project documentation


📥 Input Features

FeatureDescription
AreaProperty size (in square feet)
BedroomsNumber of bedrooms
BathroomsNumber of bathrooms


🔄 Machine Learning Workflow


Data Collection – Gathering historical housing data
Data Preprocessing – Cleaning and preparing the dataset
Feature Engineering – Selecting relevant input features
Model Training – Training a Polynomial Regression model
Model Evaluation – Assessing model performance
Model Serialization – Saving the trained model using Pickle
Application Development – Building the interface with Streamlit



⚙️ Installation & Usage

1. Clone the repository

bashgit clone https://github.com/your-username/House-Price-Prediction.git

2. Navigate to the project directory

bashcd House-Price-Prediction

3. Install the required dependencies

bashpip install -r requirements.txt

4. Run the application

bashstreamlit run app.py

The app will open in your default browser at http://localhost:8501.
