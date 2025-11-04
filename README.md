# Boston Housing Price Prediction Web App

An **end-to-end Machine Learning project** for predicting Boston housing prices using **Linear Regression**. This project includes data preprocessing, model training, building a **Flask web application**, containerizing it with **Docker**, version control using **Git & GitHub**, and deploying to **Heroku** with **GitHub Actions** CI/CD.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Software & Tools Required](#software--tools-required)  
4. [Dataset](#dataset)  
5. [Project Structure](#project-structure)  
6. [Step-by-Step Guide](#step-by-step-guide)  
7. [Deployment](#deployment)  
8. [GitHub Actions CI/CD](#github-actions-cicd)  
9. [Docker Integration](#docker-integration)  
10. [Usage](#usage)  
11. [Future Improvements](#future-improvements)  
12. [License](#license)  

---

## Project Overview

This project demonstrates the complete pipeline of a Machine Learning workflow:

- **Data Acquisition & Preprocessing:** Clean and scale the Boston Housing Dataset.  
- **Model Training:** Train a Linear Regression model to predict housing prices.  
- **Web Application:** Build a user-friendly **Flask web app** that takes input features and predicts house prices.  
- **Version Control:** Push project to **GitHub** with proper commits and branches.  
- **Containerization:** Use **Docker** to containerize the app for consistent deployment.  
- **Deployment:** Deploy the application to **Heroku** and set up automated deployment via **GitHub Actions**.  

---

## Features

- Predict Boston housing prices using 13 input features.  
- Responsive and interactive web form to accept input from users.  
- Display predicted price dynamically on the web page.  
- End-to-end workflow from model training to cloud deployment.  

---

## Software & Tools Required

- **Python 3.10+**  
- **Flask**  
- **scikit-learn**  
- **pandas & numpy**  
- **pickle** (for saving the model)  
- **Docker**  
- **Git & GitHub**  
- **Heroku account**  
- **GitHub Actions** for CI/CD  

Optional: VS Code / PyCharm for development.

---

## Dataset

**Boston Housing Dataset** contains information about housing in Boston suburbs.  

**Features:**

| Feature | Description |
|---------|-------------|
| CRIM | Per capita crime rate by town |
| ZN | Proportion of residential land zoned for lots > 25,000 sq.ft. |
| INDUS | Proportion of non-retail business acres per town |
| CHAS | Charles River dummy variable (1 if tract bounds river; 0 otherwise) |
| NOX | Nitric oxides concentration |
| RM | Average number of rooms per dwelling |
| AGE | Proportion of owner-occupied units built prior to 1940 |
| DIS | Weighted distances to five Boston employment centres |
| RAD | Index of accessibility to radial highways |
| TAX | Full-value property-tax rate per $10,000 |
| PTRATIO | Pupil-teacher ratio by town |
| B | 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town |
| LSTAT | % lower status of the population |
| MEDV | Median value of owner-occupied homes in $1000s (target) |

---

## Project Structure

boston-housing-flask/
├── app.py # Flask application
├── model.pkl # Saved Linear Regression model
├── scaler.pkl # Saved Scaler object
├── templates/
│ └── index.html # HTML form for prediction
├── static/ # (Optional) CSS/JS files
├── Dockerfile # Docker configuration
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .github/
└── workflows/
└── deploy.yml # GitHub Actions CI/CD workflow



---

## Step-by-Step Guide

### 1. Clone Repository
```bash
git clone https://github.com/your-username/boston-housing-flask.git
cd boston-housing-flask
```

### Create Virtual Environment & Install Dependencies
```
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

### Run Flask App Locally
```
heroku login
heroku create boston-housing-predictor
heroku container:push web -a boston-housing-predictor
heroku container:release web -a boston-housing-predictor
heroku open -a boston-housing-predictor
```

### Usage

  Open the deployed app in your browser.
  
  Fill all input fields with numeric values.
  
  Click Predict Price to see the predicted house price.

## Future Improvements
  Use advanced ML models (Random Forest, XGBoost) for better accuracy.
  
  Add user authentication and save predictions in a database.
  
  Improve UI with Bootstrap or React for a better user experience.
  
  Implement logging and error handling for production deployment.
