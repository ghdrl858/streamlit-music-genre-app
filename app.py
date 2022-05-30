from pyparsing import alphas
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from app_home import run_home
from app_eda import run_eda
from app_ml import run_ml

def main() :

    # 옵션 메뉴 꾸미기 코드
    with st.sidebar:
        menu = option_menu('Menu',['Home','EDA','ML'], menu_icon='caret-down-fill', icons = ['house-door-fill','bar-chart-line-fill',"bi bi-robot"], default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "black", },
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#aeacb0"},
        "nav-link-selected": {"background-color": "#9ba6fa"},
    })
    if menu == 'Home':
        run_home()
    elif menu == 'EDA':
        run_eda()
    elif menu == 'ML':
        run_ml()
   
    # 이미지 구현
    with st.sidebar :
        st.write('')
        st.write('')
        image = Image.open('image/headphones.png')
        st.image(image, use_column_width=True)