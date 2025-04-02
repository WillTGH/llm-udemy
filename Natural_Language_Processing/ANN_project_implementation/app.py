import streamlit as st
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder

#load model
model = tf.keras.models.load_model('model.h5')

## load scaler & encoders
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
    
with open('one_hot_encoder_geo.pkl', 'rb') as f:
    ohe_geo = pickle.load(f)
    
with open('label_encoder_gender.pkl', 'rb') as f:
    label_encoder_gender = pickle.load(f)
    
    
## streamlit app

st.title("Customer Churn Prediction")

geography = st.selectbox("Geography", ohe_geo.categories_[0])
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.slider('Age', 18, 100)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
tenure = st.number_input('Tenure')
num_of_products = st.number_input('Number of Products')
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])
estimated_salary = st.number_input('Estimated Salary')

## prepare input data
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender':[label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

geo_encoded = ohe_geo.transform([[input_data['Geography']]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=ohe_geo.get_feature_names_out(['Geography']))

input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

input_data_scalled = scaler.transform(input_data)

# predict

prediction = model.predict(input_data_scalled)
prediction_probability = prediction[0][0]

if prediction_probability > 0.5:
    st.write('Churn')
else:
    st.write('Not Churn')