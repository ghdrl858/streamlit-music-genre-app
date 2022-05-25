import yfinance as yf
import streamlit as st
import pandas as pd

# 작성한 문자열 앞에 '#' 의 갯수를 통해 글씨 크기 조절 가능. 갯수가 커질수록 글씨크기가 작아짐
st.write('''## Simple Stock Price App

##### shown are the stock **closing** price and ***volume*** of Apple !

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

''')

# 애플 주가 그래프
tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period = 'id', start = '2010-5-31', end = '2022-5-31')

st.write('''
## Closing Price
''')
st.line_chart(tickerDF.Close)

st.write('''
## Volume Price
''')
st.line_chart(tickerDF.Volume)