import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
import pandas_datareader.data as web
from helper_functions import interactive_plot, normalize_charts, daily_return, calculate_beta

st.set_page_config(page_title = "CAPM", page_icon = "chart_with_upwards_trend", layout='wide')
st.title('Capital Asset Pricing Model')


col1, col2 = st.columns([1, 1])
with col1:
    stocks_list = st.multiselect("Choose 4 stocks", ('TSLA', 'GOOGL', 'AAPL', 'NFLX', 'MSFT', 'MGM', 'AMZN', 'NVDA'), ['GOOGL', 'AMZN', 'AAPL', 'MSFT'])

with col2:
    year = st.number_input("Enter Number of years", 1, 10)

end = datetime.date.today()
start = datetime.date(datetime.date.today().year - year, datetime.date.today().month, datetime.date.today().day)
SP500 = web.DataReader(['sp500'], 'fred', start, end)


stocks_df = pd.DataFrame()

for stock in stocks_list:
    data = yf.download(stock, period = f'{year}y')
    stocks_df[f'{stock}'] = data['Close']

stocks_df.reset_index(inplace=True)
SP500.reset_index(inplace=True)
SP500 = SP500.rename(columns={'DATE':'Date'})

stocks_df = pd.merge(stocks_df, SP500, on='Date', how="inner")
stocks_df['Date'] = stocks_df['Date'].dt.date
col1, col2 = st.columns([1,1])

with col1:
    st.markdown("### Dataframe Head")
    st.dataframe(stocks_df.head(), use_container_width=True)

with col2:
    st.markdown("### Dataframe Tail")
    st.dataframe(stocks_df.tail(), use_container_width=True)


col1, col2 = st.columns([1,1])
with col1:
    st.markdown('### Price of all Stocks')
    st.plotly_chart(interactive_plot(stocks_df))

with col2:
    st.markdown('### Price of all Stocks (Normalized)')
    st.plotly_chart(interactive_plot(normalize_charts(stocks_df)))

stocks_daily_return = daily_return(stocks_df)

beta = {}
alpha = {}

