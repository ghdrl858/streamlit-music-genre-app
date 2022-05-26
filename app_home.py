import streamlit as st
import pandas as pd

def run_home() :
    st.write('''### Music-Genre 소개
    
###### 내용정리 잘해서 Home화면 구성해볼께요 ~

    ''')

    col1, col2, col3= st.columns(3)

    with col1 :
        st.image("image/black_elec.jpg", width = 700)