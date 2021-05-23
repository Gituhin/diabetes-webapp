#importing the libraries
import pandas as pd
import pickle
import streamlit as st

st.write("""
# Diabetes Detection
To predict is a person as diabetes using python
""")
#loading the model and segregating
data=pd.read_csv("D:\Programming\Webapp\pima-indians-diabetes.csv")
st.subheader('Data Information:')
st.dataframe(data)
st.subheader("Data Description")
st.write(data.describe())
chart = st.bar_chart(data)

def get_input():
    preg=st.sidebar.slider('pregnancies', 0, 17,13)
    plas=st.sidebar.slider('palsma', 0, 200, 50)
    bp=st.sidebar.slider('blood pressure', 0, 122, 82)
    skin=st.sidebar.slider('skin thickness', 0, 99, 20)
    insulin=st.sidebar.slider('insulin', 0, 846, 100)
    bmi=st.sidebar.slider('BMI', 0, 67, 23)
    dpf=st.sidebar.slider('dpf', 0.0, 2.45, 1.0)
    age=st.sidebar.slider('age', 21, 81, 45)

    user_data={'Preg':preg, 'plasma':plas, 'BP':bp, 'skin':skin,
                'insulin':insulin, 'bmi':bmi, 'dpf':dpf, 'age':age}
    features=pd.DataFrame(user_data, index=[0])
    return features

ui=get_input()
st.subheader('User Input')
st.write(ui)

model=pickle.load(open('D:\Programming\Webapp\web_model', 'rb'))
result='Diabetic' if model.predict(ui)==1 else 'Non-Diabetic'

st.subheader("Prediction:")
st.write(result)
#---end---