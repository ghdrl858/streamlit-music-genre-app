import streamlit as st
import pandas as pd

def run_home() :
    st.header('Music-Genre')
    # col1, col2, col3= st.columns(3)

    # with col1 :
    #     st.image("image/black_piano.jpg", width = 850)

    st.write('''##### º 다양한 장르의 음악이 여러 가지 상황과 환경에 미치는 영향을 알아봅시다.

    ''')
    video_file = open('video/guitarist-139.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)