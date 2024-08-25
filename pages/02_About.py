import streamlit as st
from PIL import Image
import webbrowser
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title='About Glaucoma', page_icon='img/logo-cakefinder.png')

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
  background-image: linear-gradient(to bottom right, #FFB6C1, #F693B4 );
}

[data-testid="stHeader"]{
  background-color: #F693B4;
}

.stButton>button {
  color: #000;
  border-radius: 10%;
  backgroud-color: #00ff00;
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

container = st.container()

with container:
  st.markdown("<h2 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>What is RetinaCheck?</h2>", unsafe_allow_html=True)
  st.markdown("""
  <p style='font-family:sans-serif; text-align:justify; margin:0; padding-top:0;'> "RetinaCheck is a website for classification of diabetic retinopathy based on medical images. 
 Our platform categorizes Glaucoma into three severity levels: Normal, early, and advanced). RetinaCheck provide accurate and 
 efficient diagnosis to help in early detection and management of Glaucoma."
  </p>"""
  , unsafe_allow_html=True)
  st.write(" ")
  if st.button("Let's Try!"):
    switch_page("Let_s Try!")
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")

#Class of Cakes
with container:
  st.markdown("<h5 style='font-family:sans-serif; text-align:center; margin-bottom:0;'>Class of</h5>", unsafe_allow_html=True)
  st.markdown("<h2 style='font-family:sans-serif; text-align:center; margin:0; padding-top:0;'>Glaucoma</h2>", unsafe_allow_html=True)
  kue1, kue2, kue3 = st.columns(3)
  with kue1:
    # st.markdown("<img src:'test/kue_dadar_gulung/5.jpg' style:'display:block; margin-left:auto; margin-right:auto; width:50%;'>", unsafe_allow_html=True)
    image = Image.open("test/normal_control3/124.png")
    new_image = image.resize((500,500))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'><a href='https://en.wikipedia.org/wiki/Diabetic_retinopathy'>Normal</a></p>", unsafe_allow_html=True)
    # if st.button('Read More'):
    #   webbrowser.open_new_tab('https://id.wikipedia.org/wiki/Dadar_gulung')
  with kue2:
    image = Image.open("test/early_glaucoma2/79.png")
    new_image = image.resize((500,500))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'><a href='https://en.wikipedia.org/wiki/Kaasstengels'>Early</a></p>", unsafe_allow_html=True)
  with kue3:
    image = Image.open("test/advanced_glaucoma1/268.png")
    new_image = image.resize((500,500))
    st.image(new_image, use_column_width=True)
    st.markdown("<p style='font-family:sans-serif; text-align:center;'><a href='https://en.wikipedia.org/wiki/Diabetic_retinopathy'>Advanced</a></p>", unsafe_allow_html=True)
  
 