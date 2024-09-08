import plotly.express as px
import numpy as np

def interactive_plot(df):
    fig = px.line()
    for i in df.columns[1:]:
        fig.add_scatter(x=df['Date'], y=df[i], name=i)
    fig.update_layout(
        width=450,
        margin=dict(l=20, r=20, t=50, b=20),
        legend=dict(orientation='h', yanchor = 'bottom', y = 1.02, xanchor = 'right', x=1),
        # title="Global COVID-19 Cases",
        # xaxis_title="Date",
        # yaxis_title="Cases",
        # hovermode="x unified"
    )
    return fig

def normalize_charts(df):
    df_normalized = df.copy()
    for i in df_normalized.columns[1:]:
        df_normalized[i] = df_normalized[i] / df_normalized[i][0]
    return df_normalized

def daily_return(df):
    df_daily_return = df.copy()
    for i in df_daily_return.columns[1:]:
        df_daily_return[i] = df_daily_return[i].pct_change() * 100
        df_daily_return[i][0] = 0
    return df_daily_return

def calculate_beta(stocks_daily_return, stock):
    b, a = np.polyfit(stocks_daily_return['sp500'], stocks_daily_return[stock], 1)
    return b, a