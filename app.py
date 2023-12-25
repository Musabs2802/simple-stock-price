import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
         # Simple Stock Price App
         Shown are the stock closing price and volumne of Google
         """)

symbol = st.selectbox('Select Stock', ('AMZN', 'AAPL', 'GOOG'), index=0)

ticker_data = yf.Ticker(symbol)
ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2020-5-31')

filter_col_1, filter_col_2 = st.columns(2)

opening_price = filter_col_1.checkbox('Opening Price')
high_price = filter_col_1.checkbox('High Price')
low_price = filter_col_1.checkbox('Low Price')
closing_price = filter_col_2.checkbox('Closing Price')
volume_price = filter_col_2.checkbox('Volumne Price')

if opening_price:
    st.write("""
            ### Opening Price
            """)
    st.line_chart(ticker_df.Open)

if high_price:
    st.write("""
            ### High Price
            """)
    st.line_chart(ticker_df.High)

if low_price:
    st.write("""
            ### Low price
            """)
    st.line_chart(ticker_df.Low)

if closing_price:
    st.write("""
            ### Closing
            """)
    st.line_chart(ticker_df.Close)

if volume_price:
    st.write("""
            ### Volume
            """)
    st.line_chart(ticker_df.Volume)
