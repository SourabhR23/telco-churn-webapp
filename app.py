import streamlit as st
import pandas as pd

# Title for the app
st.title("""
            # Customer Churn Prediction App
            This app predicts if the customer will churn or not.\n
            Data obtained from the Kaggle - [Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)
            """)

# Sidebar header
st.sidebar.header('User Input Features')
st.sidebar.markdown('[Example CSV Input file](https://github.com/SourabhR23/teleco-churn-webapp/blob/master/Telecom/churn_example.csv)')

# Collect user input features into dataframe
uploaded_file = st.sidebar.file_uploader('Upload your input CSV file', type = ['csv'])
if uploaded_file is not True:
    input_df = pd.read_csv(uploaded_file)
#else:
 #   def user_input_features():




