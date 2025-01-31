import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

import requests
from streamlit_lottie import st_lottie
import json
import streamlit.components.v1 as components

st.set_page_config(page_title='RetinaChecker', page_icon='img/logo-cakefinder.png', layout='wide')

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

container = st.container()

with container:
  home1, home2 = st.columns([11,8])
  with home1:
    st.title("We offer a modern solution for detecting Glucoma by medical image.")
    if st.button("Get Started"):
      switch_page("About")
  with home2:
    @st.cache_data
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_url = "https://assets6.lottiefiles.com/packages/lf20_bpqri9y8.json"
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json, height=400)
