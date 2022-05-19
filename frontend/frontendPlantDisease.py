import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title('Plant Disease Classification')
st.subheader('Predicting Disease using Machine Learning')
st.text('This app predicts the disease of the plant based on the features of the plant')
st.subheader('The classes are:')

col1, col2, col3 = st.columns(3)

with col1:
    st.header('Tomato')
    st.write("Tomato: Bacterial spot")
    st.write("Tomato: Early blight")
    st.write("Tomato: Late blight")
    st.write("Tomato: Leaf Mold")
    st.write("Tomato: Septoria leaf spot")
    st.write("Tomato: Spider mites Two-spotted spider mite")
    st.write("Tomato: Target Spot")
    st.write("Tomato: Yellow leaf curl virus")
    st.write("Tomato: Mosaic Virus")
    st.write("Tomato: healthy")

with col2:
    st.header('Potato')
    st.write("Potato: Early blight")
    st.write("Potato: Late blight")
    st.write("Potato: healthy")

with col3:
    st.header('Pepper')
    st.write("Pepper bell: Bacterial spot")
    st.write("Pepper bell: healthy")




hide_streamlit_style = "<style>footer {visibility: hidden;}</style>"
st.markdown(hide_streamlit_style, unsafe_allow_html=True)\


def main():
    st.sidebar.header('User Input Parameters')
    image = st.sidebar.file_uploader("Upload an image...", type=['jpg', 'png', 'jpeg'])
    if image is not None:
        st.sidebar.subheader('Image uploaded!')
        st.sidebar.image(image, use_column_width=True)                   
        r=requests.post('http://localhost:8000/predict', files={'file': image})
        response=r.json()
        st.sidebar.subheader('Prediction')
        st.sidebar.text('The predicted class is: {}'.format(response['class']))
        #round of the confidence to 2 decimal places
        st.sidebar.text('The confidence is: {}'.format(round(response['confidence']*100,2)))
    else:
        st.sidebar.warning('Please upload an image')




    

main()
