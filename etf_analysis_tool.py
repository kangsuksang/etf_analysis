import streamlit as st
import yfinance as yf
import pandas as pd

st.title("US ETF Analysis Tool")

etf_ticker = st.text_input("Enter ETF Ticker: ")

if etf_ticker:
    etf_data = yf.Ticker(etf_ticker)
    etf_info = etf_data.info
    st.table(pd.DataFrame.from_dict(etf_info, orient='index'))

    hist = etf_data.history(period="1y")
    st.line_chart(hist["Close"])

    etf_holdings = etf_data.major_holders
    st.table(etf_holdings)

