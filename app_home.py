import streamlit as st
import pandas as pd

def run_home() :
    st.header('Music-Genre')
    # col1, col2, col3= st.columns(3)

    # with col1 :
    #     st.image("image/black_piano.jpg", width = 850)

    st.write('''#### º 

    ''')
    video_file = open('video/Guitarist - 139.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)