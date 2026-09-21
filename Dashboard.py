import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("CarPurchaseAmount.pkl", "rb"))

st.title(":red[Car Purchase Amount Prediction]")

annualSalary = st.number_input("annual Salary")
creditcarddebt = st.number_input("credit card debt")
networth = st.number_input("net worth")

carmodel = st.selectbox("car model", ["base", "medium", "top"])
car_map = {"base": 0, "medium": 1, "top": 2}
carmodel = car_map[carmodel]

Fuel = st.selectbox("Fuel", ["Petrol", "Diesel"])
Fuel = 1 if Fuel == "Petrol" else 0

Brand = st.selectbox("Brand", ["AUDI","KIA","MAHINDRA","MARUTI","TATA","TOYOTA"])
Brand_map = {"AUDI": 0, "KIA": 1, "MAHINDRA": 2, "MARUTI": 3,'TATA':4,'TOYOTA':5}
Brand = Brand_map[Brand]


Noofseats = st.number_input("No. of seats")

Transmission = st.selectbox("Transmission", ["Manual","Automatic"])
Transmission = 1 if Transmission == "Manual" else 0

Mileage = st.number_input("Mileage")

if st.button("Predict Car Purchase Amount"):
    input_data = np.array([[annualSalary,creditcarddebt,networth,carmodel,Fuel,Brand,Noofseats,Transmission,Mileage]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Car Purchase Amount: ₹ {prediction[0]}")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://acko-cms.ackoassets.com/how_much_to_spend_on_a_car_in_India_4654e7ea90.png");
    background-size: cover;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("""
    <style>
    /* Target all standard text elements */
    p, div, label {
        color: #FFFF00;
    }
    </style>
    """, unsafe_allow_html=True)
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
df=pd.read_csv('car.csv')
# Calculate the correlation matrix
corr = df.corr(numeric_only=True)

# Create the matplotlib figure
fig, ax = plt.subplots(figsize=(10, 6))

# Generate the heatmap on the specific axes (ax)
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
ax.set_title("Feature Correlation Heatmap")

# Display the figure in Streamlit
st.pyplot(fig)
