import streamlit as st
import pandas as pd
import yfinance as yf
from PIL import Image
from app_home import run_home
from app_eda import run_eda
from app_ml import run_ml

def main() :

    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_ml()
    
    with st.sidebar :
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        image = Image.open('image/headphones.png')
        st.image(image, use_column_width=True)
    #     tickerSymbol = 'MSFT'

    #     tickerData = yf.Ticker(tickerSymbol)

    #     tickerDF = tickerData.history(period = 'id', start = '2012-5-31', end = '2022-5-31')

    #     st.write('''
    #     ## Closing Price
    #     ''')
    #     st.line_chart(tickerDF.Close)

if __name__ == '__main__' :
    main()