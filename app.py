# Importing required libraries
import pandas as pd
import numpy as np
import streamlit as st
import pickle as pk

# Loading the pre-trained model
model = pk.load(open(r"C:\Users\yhima\Desktop\Temp 2\Heart_disease_model.pkl","rb"))

# Loading the dataset
df = pd.read_csv(r"C:\Users\yhima\Desktop\Temp 2\heart_disease.csv")

# Setting up the Streamlit app
st.header("Heart Disease Predictor")

# Input fields for user to enter information
gender = st.selectbox("Choose Gender", df["Gender"].unique())
if gender == "Male":
    gen = 1
else:
    gen = 0

age = st.number_input("Enter Age in Years")
currentSmoker = st.number_input("Is patient a currentSmoker? (0 = N0, 1 = YES)")
cigsPerDay = st.number_input("Enter cigsPerDay")
BPMeds = st.number_input("Is patient on BPMeds? (0 = N0, 1 = YES)")
prevalentStroke = st.number_input("Is patient had prevalentStroke? (0 = N0, 1 = YES)")
prevalentHyp = st.number_input("Enter prevalentHyp status (0 = N0, 1 = YES)")
diabetes = st.number_input("Enter diabetes ststus (0 = N0, 1 = YES)")
totChol = st.number_input("Enter totChol")
sysBP = st.number_input("Enter sysBP")
diaBP = st.number_input("Enter diaBP")
BMI = st.number_input("Enter BMI")
heartRate = st.number_input("Enter heartRate")
glucose = st.number_input("Enter glucose")

# Making prediction when user clicks the button
if st.button("PREDICT"):
    # Prepare input for prediction
    input_data = np.array([[gen, age, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose]])

    # Making prediction
    prediction = model.predict(input_data)

    # Displaying prediction result
    if prediction[0] == 0:
        st.write("Patient is Healthy, No Heart Disease")
    else:
        st.write("Patient may have Heart Disease")
