import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title('Plant Disease Classification')
st.subheader('Predicting Disease using Machine Learning')
st.text('This app predicts the disease of the plant based on the features of the plant')
st.subheader('The classes are:')

st.write("Pepper bell: Bacterial spot")
st.write("Pepper bell: healthy")
st.write("Potato: Early blight")
st.write("Potato: Late blight")
st.write("Potato: healthy")
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


def main():
    st.sidebar.header('User Input Parameters')
    image = st.sidebar.file_uploader("Upload an image...", type=['jpg', 'png', 'jpeg'])
    if image is not None:
        st.sidebar.subheader('Image uploaded')
        st.sidebar.image(image, use_column_width=True)                
        r=requests.post('http://127.0.0.1:5000/predict', files={'file': image})
        response=r.json()
        st.sidebar.subheader(response)
        class_name=response['class']
        confidence=response['confidence']
        st.sidebar.subheader('Class and Confidence')
        st.sidebar.text('Class: {}'.format(class_name))
        st.sidebar.text('Confidence: {}'.format(confidence))


    else:
        st.sidebar.warning('Please upload an image')
    hide_streamlit_style = "<style>footer {visibility: hidden;}</style>"
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

main()
