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
st.sidebar.markdown('[Example CSV Input file]()')