import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Title for the app
st.title("""
            # Customer Churn Prediction App
            This app predicts if the customer will churn or not.\n
            Data obtained from the Kaggle - [Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)
            """)

# Sidebar header
st.sidebar.header('User Input Features')
st.sidebar.markdown('[Example CSV Input file](https://github.com/SourabhR23/teleco-churn-webapp/blob/master/Telecom'
                    '/churn_example.csv)')

# Collect user input features into dataframe
uploaded_file = st.sidebar.file_uploader('Upload your input CSV file', type = ['csv'])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    st.sidebar.write('Enter the data manually')

    def user_input_features():
        gender = st.sidebar.selectbox('Gender', ('Male', 'Female'))
        senior = st.sidebar.selectbox('Senior Citizen', (1, 0))
        partner = st.sidebar.selectbox('Partner', ('Yes', 'No'))
        dependents = st.sidebar.selectbox('Dependents', ('Yes', 'No'))
        tenure = st.sidebar.slider('Tenure', 0, 72, 47)
        phone_service = st.sidebar.selectbox('Phone Service', ('Yes', 'No'))
        multi_lines = st.sidebar.selectbox('Multiple Lines', ('Yes', 'No', 'No phone service'))
        internet = st.sidebar.selectbox('Internet Service', ('DSL', 'Fiber optic', 'No'))
        online_sec = st.sidebar.selectbox('Online Security', ('Yes', 'No', 'No internet service'))
        online_back = st.sidebar.selectbox('Online Backup', ('Yes', 'No', 'No internet service'))
        dev_protect = st.sidebar.selectbox('Device Protection', ('Yes', 'No', 'No internet service'))
        tech_sup = st.sidebar.selectbox('Tech Support', ('Yes', 'No', 'No internet service'))
        stream_tv = st.sidebar.selectbox('Streaming TV', ('Yes', 'No', 'No internet service'))
        stream_movie = st.sidebar.selectbox('Streaming Movies', ('Yes', 'No', 'No internet service'))
        contract = st.sidebar.selectbox('Contract', ('Month-to-month', 'One year', 'Two year'))
        paperless_bill = st.sidebar.selectbox('Paperless Billing', ('Yes', 'No'))
        payment = st.sidebar.selectbox('Payment Method', ('Electronic check', 'Mailed check',
                                                          'Bank transfer (automatic)',
                                                          'Credit card (automatic)'))
        monthly_charge = st.sidebar.number_input('Monthly Charges', 18.25, 119.0, 56.75)
        total_charge = st.sidebar.number_input('Total Charges', 0.0, 8684.8, 1556.75)
        # creating dictionary for DataFrame reference
        data = {'gender': gender,
                'SeniorCitizen': senior,
                'Partner': partner,
                'Dependents': dependents,
                'tenure': tenure,
                'PhoneService': phone_service,
                'MultipleLines': multi_lines,
                'InternetService': internet,
                'OnlineSecurity': online_sec,
                'OnlineBackup': online_back,
                'DeviceProtection': dev_protect,
                'TechSupport': tech_sup,
                'StreamingTV': stream_tv,
                'StreamingMovies': stream_movie,
                'Contract': contract,
                'PaperlessBilling': paperless_bill,
                'PaymentMethod': payment,
                'MonthlyCharges': monthly_charge,
                'TotalCharges': total_charge}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

# Combining the user input features with entire churn dataset
# This will be useful for the encoding phase
raw_churn_data = pd.read_csv(r'Telecom/Churn.csv')
raw_churn_data = raw_churn_data.drop(columns = ['customerID', 'Churn'])
df = pd.concat([input_df, raw_churn_data], axis = 0)

# Encoding of the ordinal features
encode = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
          'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
          'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
          'PaperlessBilling', 'PaymentMethod']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix = col, drop_first = True)
    df = pd.concat([df, dummy], axis = 1)
    del df[col]
# Select only the first row (the user input data)
df = df[: 1]
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])

# Displays the user input features
st.subheader('User Input features')
if uploaded_file:
    st.write(input_df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using below example.')
    st.write(input_df.iloc[:, :5])
    st.write(input_df.iloc[:, 6: 11])
    st.write(input_df.iloc[:, 11: 15])
    st.write(input_df.iloc[:, 15:])

# Load the saved model
load_clf = pickle.load(open('Model/modelForPrediction.sav', 'rb'))

# Apply model on the prediction
st.subheader('Prediction')
st.write('Hit "Predict" button to run the app!')
predict = st.button('Predict')
if predict:
    # predictions
    prediction = load_clf.predict(df)
    prediction_proba = load_clf.predict_proba(df)[:,0]

    # output results
    if prediction == 1:
        st.write('This customer is likely to be churned.')
        st.write(f'Confidence: {prediction_proba * 100}')
    else:
        st.write('This customer is likely to continue with the service.')
        st.write(f'Confidence: {prediction_proba * 100}')

