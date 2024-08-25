import streamlit as st
import numpy as np
import cv2 as cv
import os
from io import BytesIO
import tensorflow as tf
from PIL import Image
from tensorflow.keras.layers import *
from tensorflow.keras.models import *
import time

# import streamlit.components.v1 as com

st.set_page_config(page_title='Try it!', page_icon='img/logo-cakefinder.png', layout='wide')

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
  background-image: linear-gradient(to bottom right, #FFB6C1, #F693B4);
}

[data-testid="stHeader"]{
  background-color: #F693B4;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>GLAUCOMA DIAGNOSIS</h5>", unsafe_allow_html=True)
st.markdown("<h2 style='font-family:sans-serif; text-align:center; margin:0; padding-top:0;'>Upload Your Picture</h2>", unsafe_allow_html=True)
  
from tensorflow.keras.applications import ResNet50

###Input Image
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    #st.write("nama file yang diupload = ", uploaded_file.name)
    #ini untuk nampilin gambar, outputnya bytes
    bytes_image = uploaded_file.read() #baca image

    #nampilin gambar
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(" ")
    with col2:
        image = Image.open(BytesIO(bytes_image))
        st.image(image, use_column_width=True)
    with col3:
        st.write(" ")

    image_np = np.asarray(image)
    #Assuming your model expects Input shape (None, 64, 64, 1), biar input sesuai sama inputan awal. Kalo ndak sesuai nanti error
    resized_image = cv.resize(image_np, (224,224))
    resized_image = np.expand_dims(resized_image, axis=-1) #add a new dimension
    resized_image = np.expand_dims(resized_image, axis=0)

    num_classes = 5
    input_shape = (224, 224, 3)
    learning_rate = 0.0001
    weight_decay = 0.0001
    batch_size = 32
    num_epochs = 50

    IMG_SHAPE = (224, 224, 3)
    IMG_SHAPE = (224, 224, 3)
    # Membuat model dasar (base model) dari pre-trained model VGG-16Net
    base_model2 = tf.keras.applications.VGG16(input_shape=IMG_SHAPE,
                                                include_top=False, 
                                                weights='imagenet')
    base_model2.trainable = False
    base_model2.summary()

    from tensorflow.keras.optimizers import Adam
    from tensorflow.keras import regularizers
    def create_model1():
        model = tf.keras.Sequential([
            base_model2,
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(512, activation='relu'),
            tf.keras.layers.Dense(512, activation='relu'),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(3, activation='softmax')
        ])
        return model
    model1 = create_model1()
    
    model1.load_weights("cnn.h5")

    #Proses
    result = model1.predict(resized_image)
    # output = np.rint(result)


    #Proses
    result = model1.predict(resized_image)
    # output = np.rint(result)

    with st.spinner('Wait for it...'):
        time.sleep(5)
    st.success('Done!')

    hasil = np.argmax(result)
    # st.text(hasil)

    if hasil==0:
        st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Normal;</h5>", unsafe_allow_html=True)
    elif hasil==1:
        st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Early</h5>", unsafe_allow_html=True)
    elif hasil==2:
        st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Advanced</h5>", unsafe_allow_html=True)
    else:
        st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Tidak Diketahui</h5>", unsafe_allow_html=True)