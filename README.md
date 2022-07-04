<h1 align="center"> Plant Disease Classification </h1>

<h3 align="left"> About </h3>
<p align="left">
    The goal of the project is to classify the disease of a plant based on the features of the plant. </br>
    The model during training reached an accuracy of 96% after training on 16,512 images of plant-kingdom dataset available on Kaggle. It was futher validated and tested against 4,096 images. The model was trained for 30 epochs, as 50 epochs resulted in overfitting. The model currently consists of a convolutional neural network with a single hidden layer. The model is trained using the Adam optimizer. It is able to predict 15 different classes of diseases. </br>
    Using the application developed using streamlit, it is possible to classify the disease of a plant using the image of the plant. The image can be uploaded from the computer or from the camera. The image is then converted to a tensor and passed to the model for prediction. The predicted class is then displayed on the screen along with the confidence. </br>


<img src="https://i.ibb.co/rpqc82s/streamlit.png" alt="streamlit" border="0" height="350" width="440">
<img src="https://i.ibb.co/vZg74zq/streamlit2.png" alt="streamlit2" border="0" height="350" width="420">

<h3 align="left"> Run locally </h3>
<ul>
    <li> Install <a href="https://www.python.org/"> Python </a> </li>
    <li> Install pipenv using 'pip install pipenv'</li>
    <li> cd to the project directory </li>
    <li> Install the dependencies using ```pipenv install -r requirements.txt```</li>
    <li> cd to streamlitFrontend directory </li>
    <li> Run the code using ```streamlit run predictDisease.py```</li>
</ul>

<h3 align="left"> Roadmap </h3>
<ul>
    <li> Develop a GUI using React.js </li>
    <li> Work on an API to communicate with the model (currently ongoing using FastAPI) and deploy the API on a server</li>
    <li> Work on a basic mobile app using flutter to enable live scanning of plants </li>
    <li> Futher improve the performance by studying and using adequate classifiers and optimizers </li>
    <li> Expand the dataset to include more images </li>
</ul>

<h3 align="left"> Libraries used </h3>
<ul>
    <li> <a href="https://www.python.org/"> Python </a> </li>
    <li> <a href="https://www.pipenv.com/"> Pipenv </a> </li>
    <li> <a href="https://www.numpy.org/"> Numpy </a> </li>
    <li> <a href="https://matplotlib.org/"> Matplotlib </a> </li>
    <li> <a href="https://streamlit.io/"> Streamlit </a> </li>
    <li> <a href="https://keras.io/"> Keras </a> </li>
    <li> <a href="https://www.tensorflow.org/"> Tensorflow </a> </li>
    <li> <a href="https://www.kaggle.com/"> Kaggle </a> </li>
    <!-- <li> <a href="https://altair-viz.github.io/"> Altair </a> </li> -->
    <!-- <li> <a href="https://plotly.com/"> Plotly </a> </li> -->
</ul>