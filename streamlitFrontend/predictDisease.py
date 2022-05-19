import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
from io import BytesIO

MODEL = tf.keras.models.load_model("../models/1")

CLASS_NAMES = ['Pepper__bell___Bacterial_spot',
 'Pepper__bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Tomato_Bacterial_spot',
 'Tomato_Early_blight',
 'Tomato_Late_blight',
 'Tomato_Leaf_Mold',
 'Tomato_Septoria_leaf_spot',
 'Tomato_Spider_mites_Two_spotted_spider_mite',
 'Tomato__Target_Spot',
 'Tomato__Tomato_YellowLeaf__Curl_Virus',
 'Tomato__Tomato_mosaic_virus',
 'Tomato_healthy']

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
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image
def main():
    st.sidebar.header('User Input Parameters')
    image = st.sidebar.file_uploader("Upload an image...", type=['jpg', 'png', 'jpeg'])
    if image is not None:
        st.sidebar.subheader('Image uploaded!')
        st.sidebar.image(image, use_column_width=True)    
        image=read_file_as_image(image.read())               
        image = tf.image.resize(image, (256, 256))
        img_batch = np.expand_dims(image, 0)

        predictions = MODEL.predict(img_batch)

        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])
        st.sidebar.subheader('Prediction')
        st.sidebar.success('The predicted class is: {}'.format(predicted_class))
        st.sidebar.success('The confidence is: {}'.format(round(confidence*100, 2)))
    else:
        st.sidebar.warning('Please upload an image')




    

main()
