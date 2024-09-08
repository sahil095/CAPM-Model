import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(page_title = "CAPM", page_icon = "chart_with_upwards_trend", layout='wide')
st.title('Capital Asset Pricing Model')

stocks_list = st.multiselect("Choose 4 stocks", ('TSLA', 'GOOGL', 'AAPL', 'NFLX', 'MSFT', 'MGM', 'AMZN', 'NVDA'), ['GOOGL', 'AMZN', 'AAPL', 'MSFT'])

years = st.number_input("Enter Number of years", 1, 10)