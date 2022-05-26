import streamlit as st
import pandas as pd
from app_home import run_home
# from app_eda import run_eda
from app_ml import run_ml

def main() :
    st.header('Music-Genre')

    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        # run_eda()
        pass
    elif choice == menu[2] :
        run_ml()

if __name__ == '__main__' :
    main()