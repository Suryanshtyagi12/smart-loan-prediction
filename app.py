import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

st.title("Smart Loan Prediction System")

gender = st.selectbox('Gender', ['Male', 'Female'])
married = st.selectbox('Married', ['Yes', 'No'])
education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
applicant_income = st.number_input('Applicant Income')
loan_amount = st.number_input('Loan Amount')

gender = 1 if gender == 'Male' else 0
married = 1 if married == 'Yes' else 0
education = 1 if education == 'Graduate' else 0

if st.button('Predict Loan Status'):
    features = np.array([[gender, married, education, applicant_income, loan_amount]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("✅ Loan will be Approved")
    else:
        st.error("❌ Loan will NOT be Approved")
