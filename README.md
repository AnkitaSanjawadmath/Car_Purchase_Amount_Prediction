# Car_Purchase_Amount_Prediction
This repository features a machine learning regression model designed to predict customer spending behavior. By analyzing key customer data including annual salary, net worth, and other financial metrics. The model predicts the total amount a customer is likely to spend on a vehicle purchase.
# Car Purchase Amount Predictor (Streamlit Dashboard)

## 📖 Project Overview

### 1. Introduction to Prediction Model
Sales prediction is a critical task in business analytics. Companies leverage customer data such as salary, net worth, and financial profiles to predict purchasing behavior. In this project, we utilize a car purchasing dataset to predict how much a customer is likely to spend on a vehicle using machine learning techniques.

### 2. Real-World Application
This system provides actionable insights across multiple domains, helping businesses understand customer spending patterns and improve sales strategies:
* **Automobile Companies:** Used for long-term sales forecasting.
* **Marketing & Sales Teams:** Enables precision targeting and optimized sales planning.
* **E-Commerce Platforms & Retail:** Powers customer behavior analysis and personalized product placement.
* **Business Intelligence Systems:** Integrates data-driven purchasing metrics into corporate dashboards.

### 3. Problem Statement
Businesses want to predict customer purchasing power to improve sales planning and marketing decisions. However, manual analysis of complex customer financial data is highly difficult, inefficient, and time-consuming. Therefore, a machine learning solution is required to automate and accurately forecast these patterns.

### 4. Objective of the Project
* **Analyze** customer financial and demographic profiles.
* **Understand** the key underlying factors affecting a customer's final car purchase amount.
* **Perform** Exploratory Data Analysis (EDA) and visualize key data insights.
* **Build** a robust **Supervised Machine Learning Regression** model, chosen because the target variable (*car purchase amount*) is a continuous numerical value.

---

## 🛠️ Repository Structure

```text
├── CarPurchaseAmount.ipynb  # Jupyter Notebook for EDA, visualization, and model training
├── Model.pkl                  # The trained, serialized regression model
└── Dashboard.py                # Streamlit web application script loading the pickle file
```

---

## 🚀 Installation & Setup

Follow these steps to set up the environment and run the dashboard locally on your machine.

### 1. Clone the Repository
```bash
git clone https://github.com
cd your-repo-name
```

### 2. Create a Virtual Environment (Recommended)
```bash
# On Mac/Linux:
python -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
Ensure you install `streamlit` alongside the core machine learning libraries so the dashboard can execute seamlessly:
```bash
pip install streamlit scikit-learn pandas numpy
```

---

## 💻 Running the Streamlit Dashboard

The trained regression model is saved in the `model.pkl` file using Python's `pickle` library. The `Dashboard.py` file builds an interactive user interface using Streamlit, capturing user parameters and producing predictions in real-time.

To launch the dashboard, open your terminal and run the following command:
```bash
streamlit run predict.py
```

Once executed, a browser window will automatically open (usually at `http://localhost:8501`) displaying your interactive prediction dashboard.

### Under the Hood: How Streamlit & Pickle Work Together
Inside your `predict.py` file, the app reads the serialized pickle file and handles user input dynamically:
```python
#import streamlit as st
#import pickle

# Load the serialized regression model
#model = pickle.load(open("CarPurchaseAmount.pkl", "rb"))

# Streamlit input interface example
#annualSalary = st.number_input("annual Salary")
#creditcarddebt = st.number_input("credit card debt")

# Generate continuous prediction upon user action
#if st.button("Predict Car Purchase Amount"):
#input_data = np.array([[annualSalary,creditcarddebt,networth,carmodel,Fuel,Brand,Noofseats,Transmission,Mileage]])
#prediction = model.predict(input_data)
#st.success(f"Predicted Car Purchase Amount: ₹ {prediction[0]}")
```
