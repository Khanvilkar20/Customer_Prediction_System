# Customer Purchase Prediction using Machine Learning

## 📌 Project Overview

Customer Purchase Prediction is an end-to-end Machine Learning application that predicts whether a customer is likely to purchase a product based on their browsing behavior and purchase history.

The project simulates a real-world e-commerce scenario by generating synthetic customer data, storing it in a MySQL database, training a Random Forest Classifier, and deploying an interactive prediction interface using Streamlit.

---

## 🎯 Objective

The primary objective of this project is to analyze customer behavior and predict purchase intent using Machine Learning. The system helps businesses identify potential buyers based on user activity such as website engagement, browsing time, and previous purchases.

---

## 🚀 Features

- Customer purchase prediction using Machine Learning
- Synthetic customer dataset generation
- MySQL database integration
- Data preprocessing and feature encoding
- Random Forest Classification model
- Interactive Streamlit web application
- Real-time prediction interface
- End-to-end ML pipeline implementation

---

## 🛠 Tech Stack

### Programming Language
- Python

### Database
- MySQL

### Machine Learning
- Scikit-learn
- Random Forest Classifier

### Data Processing
- Pandas
- NumPy

### Frontend
- Streamlit

### Database Connectivity
- mysql-connector-python

### Model Serialization
- Joblib

### Dataset Generation
- Faker
- Random

### Development Environment
- Visual Studio Code
- MySQL Workbench

---

## 🏗 System Architecture

```
User
   │
   ▼
Streamlit Web Application
   │
   ▼
Trained ML Model (model.pkl)
   │
   ▼
Random Forest Classifier
   ▲
   │
Training Dataset
   ▲
   │
Pandas DataFrame
   ▲
   │
MySQL Database
```

---

## 📂 Project Structure

```
customer-purchase-prediction/

│── model/
│   └── model.pkl
│
│── generate_data.py
│── train_model.py
│── app.py
│── requirements.txt
│── README.md
│
└── MySQL Database
     └── customer_activity
```

---

## 🗄 Database Design

### Database

```
customer_db
```

### Table

```
customer_activity
```

| Column | Data Type |
|----------|------------|
| customer_id | INT (Primary Key) |
| age | INT |
| gender | VARCHAR |
| pages_viewed | INT |
| time_spent | INT |
| previous_purchases | INT |
| product_category | VARCHAR |
| purchased | INT |

---

## 📊 Dataset Information

The project uses a synthetic dataset generated using Python.

**Total Records:** 1000

**Total Features:** 6

**Target Variable:** purchased

### Features

- Age
- Gender
- Pages Viewed
- Time Spent
- Previous Purchases
- Product Category

### Target

```
Purchased

0 = No

1 = Yes
```

---

## 📈 Data Generation

Customer data is generated using:

- Faker
- Random

Business logic is used to simulate customer purchase behavior based on:

- Website engagement
- Browsing duration
- Purchase history

This approach creates realistic customer interaction data for model training.

---

## ⚙ Data Preprocessing

The following preprocessing steps were performed:

- Reading data from MySQL
- Handling structured data using Pandas
- Label Encoding categorical variables
- Feature selection
- Train-Test split (80:20)

---

## 🤖 Machine Learning Model

Algorithm Used:

**Random Forest Classifier**

### Why Random Forest?

- Handles structured data effectively
- Reduces overfitting
- High classification accuracy
- Ensemble learning approach
- Suitable for binary classification problems

---

## 📊 Model Evaluation

Evaluation Metric:

- Accuracy Score

Dataset Split:

- Training Data: 80%
- Testing Data: 20%

Model Accuracy:

```
100%
```

> **Note:** The dataset is synthetically generated using deterministic business rules, resulting in perfect accuracy. Real-world datasets would produce more realistic accuracy values.

---

## 💾 Model Deployment

The trained model is serialized using Joblib.

```
model.pkl
```

The saved model is loaded directly into the Streamlit application for real-time predictions without retraining.

---

## 🖥 User Interface

The Streamlit application allows users to enter:

- Age
- Gender
- Pages Viewed
- Time Spent
- Previous Purchases
- Product Category

The application predicts whether the customer is likely to purchase the product.

---

## 🔄 Workflow

```
Generate Synthetic Dataset
        │
        ▼
Store Data in MySQL
        │
        ▼
Load Data using Pandas
        │
        ▼
Preprocess Dataset
        │
        ▼
Encode Features
        │
        ▼
Split Dataset (80:20)
        │
        ▼
Train Random Forest Model
        │
        ▼
Evaluate Model
        │
        ▼
Save Model (model.pkl)
        │
        ▼
Deploy using Streamlit
        │
        ▼
Real-Time Customer Purchase Prediction
```

---

## 📦 Installation

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the data generation script

```bash
python generate_data.py
```

Train the model

```bash
python train_model.py
```

Launch the Streamlit application

```bash
streamlit run app.py
```

---

## 📚 Skills Demonstrated

- Python Programming
- SQL & MySQL Database
- Machine Learning
- Random Forest Classification
- Data Preprocessing
- Feature Engineering
- Database Integration
- Model Evaluation
- Model Serialization
- Streamlit Application Development
- End-to-End ML Pipeline

---

## 🚀 Future Enhancements

- Integration with real-world customer datasets
- Hyperparameter tuning
- Probability-based purchase prediction
- REST API development using FastAPI
- User authentication
- Power BI analytics dashboard
- Cloud deployment on AWS or Azure

---

## 👨‍💻 Author

**Sahil**

Customer Purchase Prediction using Machine Learning

Developed as part of a Machine Learning Hackathon to demonstrate end-to-end data engineering, machine learning, database integration, and web application deployment.
