import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import date
import yfinance as yf

st.title('Index Funds vs Major Corporation Stocks')

stocks = ('AAPL', 'MSFT', 'GOOG', 'VFIAX', 'SWPPX', 'VOO')
Start = '2017-10-19'
today = date.today().strftime("%Y-%m-%d")

# Creates a Function that takes stock symbols and creates a dataframe
def load_ticker(ticker):
    data = yf.download(ticker, Start, today)
    data.reset_index(inplace=True)

    df1 = data[data['Date'] == '2017-10-20']
    df2 = data[data['Date'] == '2018-11-20']
    df3 = data[data['Date'] == '2019-11-20']
    df4 = data[data['Date'] == '2020-10-20']
    df5 = data[data['Date'] == '2021-10-20']
    df6 = data[data['Date'] == '2022-10-20']

    list_dfs = [df1, df2, df3, df4, df5, df6]
    merged_df = pd.concat(list_dfs)
    merged_df.reset_index(inplace=True)
    merged_df = merged_df.drop(['index'], axis=1)
    return merged_df

# Creates a dataframe of all of the stocks: open, close, volume, lows, highs
data = load_ticker(stocks)

st.subheader('Shows the change in price over 5 years')
st.write(data)

# Creates a Line Graph showing the High and Low Points from each day
all_stocks_low = px.line(data['Low'])
all_stocks_high = px.line(data['High'])
st.header('Stock Lows')
st.write(all_stocks_low)
st.header('Stock Highs')
st.write(all_stocks_high)

data = load_ticker(stocks)

# Creates a drop down menu to compare Relative Returns between stocks
st.header('Comparing Relative Returns')
st.subheader('Choose from the dropdown menu to compare relative returns')
def relative_return(df):
    rel = df.pct_change()
    cumret = (1-rel).cumprod()-1
    cumret = cumret.fillna(0)
    return cumret

dropdown = st.multiselect('Pick Your Assets', stocks)
start = st.date_input('Start', value = pd.to_datetime('2017-01-01'))
end = st.date_input('End', value = pd.to_datetime('today'))

if len(dropdown) > 0:
    df = relative_return(yf.download(dropdown, Start, today)['Adj Close'])
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(df)

st.sidebar.title('Options')
st.sidebar.header('Which stock would you like to see?')
option = st.sidebar.selectbox("Graph of Stocks and Index Funds: ", ('Apple', 'Microsoft', 'Google', 'Vanguard 500 Index Fund', 'Schwab S&P 500 Index Fund', 'Vanguard S&P 500 ETF'))

st.header(option)
st.write('Objective: To do Data Analysis and figure out which made more in the long run: stocks or the indexes that follow them.')

if option == 'Apple':
    st.subheader('Apple Stocks')
    data_load = st.text('Loading...')
    apple_data = yf.download("AAPL", Start, today)
    data_load.text('Loading Data...Done!')

    apple_data.reset_index(inplace=True)

    df1 = apple_data[apple_data['Date'] == '2017-10-20']
    df2 = apple_data[apple_data['Date'] == '2018-11-20']
    df3 = apple_data[apple_data['Date'] == '2019-11-20']
    df4 = apple_data[apple_data['Date'] == '2020-10-20']
    df5 = apple_data[apple_data['Date'] == '2021-10-20']
    df6 = apple_data[apple_data['Date'] == '2022-10-20']

    list_dfs = [df1, df2, df3, df4, df5, df6]
    merged_df = pd.concat(list_dfs)
    merged_df.reset_index(inplace=True)
    merged_df = merged_df.drop(['index'], axis=1)

    st.subheader('Shows the change in price over 5 years')
    st.write(merged_df)
    fig = px.line(apple_data['Open'],  title='Apple Stock Value')
    fig.update_yaxes(title_text='Value ($)')
    fig.update_traces(line_color='#FF0000')
    st.write(fig)

    # Creates a Histogram with the Volume of Trades
    st.subheader('Apple Volume')
    apple_volume = apple_data['Volume']
    fig1 = px.histogram(apple_volume, color_discrete_sequence = ['red'])
    st.write(fig1)

elif option == 'Microsoft':
    st.subheader('Microsoft Stocks')
    data_load = st.text('Loading...')
    msft_data = yf.download("MSFT", Start, today)
    data_load.text('Loading Data...Done!')

    msft_data.reset_index(inplace=True)

    df1 = msft_data[msft_data['Date'] == '2017-10-20']
    df2 = msft_data[msft_data['Date'] == '2018-11-20']
    df3 = msft_data[msft_data['Date'] == '2019-11-20']
    df4 = msft_data[msft_data['Date'] == '2020-10-20']
    df5 = msft_data[msft_data['Date'] == '2021-10-20']
    df6 = msft_data[msft_data['Date'] == '2022-10-20']

    list_dfs = [df1, df2, df3, df4, df5, df6]
    merged_df = pd.concat(list_dfs)
    merged_df.reset_index(inplace=True)
    merged_df = merged_df.drop(['index'], axis=1)

    st.subheader('Shows the change in price over 5 years')
    st.write(merged_df)
    fig = px.line(msft_data['Open'], title='Microsoft Stock Value')
    fig.update_yaxes(title_text='Value ($)')
    st.write(fig)

    # Creates a Histogram with the Volume of Trades
    st.subheader('Microsoft Volume')
    msft_volume = msft_data['Volume']
    fig1 = px.histogram(msft_volume, color_discrete_sequence = ['aqua'])
    fig1.update_yaxes(title_text='Volume')
    st.write(fig1)

elif option == 'Google':
    st.subheader('Google Stocks')
    data_load = st.text('Loading...')
    google_data = yf.download("GOOG", Start, today)
    data_load.text('Loading Data...Done!')

    google_data.reset_index(inplace=True)

    df1 = google_data[google_data['Date'] == '2017-10-20']
    df2 = google_data[google_data['Date'] == '2018-11-20']
    df3 = google_data[google_data['Date'] == '2019-11-20']
    df4 = google_data[google_data['Date'] == '2020-10-20']
    df5 = google_data[google_data['Date'] == '2021-10-20']
    df6 = google_data[google_data['Date'] == '2022-10-20']

    list_dfs = [df1, df2, df3, df4, df5, df6]
    merged_df = pd.concat(list_dfs)
    merged_df.reset_index(inplace=True)
    merged_df = merged_df.drop(['index'], axis=1)

    st.subheader('Shows the change in price over 5 years')
    st.write(merged_df)
    fig = px.line(google_data['Open'], title='Google Stock Value')
    fig.update_yaxes(title_text='Value ($)')
    fig.update_traces(line_color='green')
    st.write(fig)

    # Creates a Histogram with the Volume of Trades
    st.subheader('Google Volume')
    google_volume = google_data['Volume']
    fig1 = px.histogram(google_volume, color_discrete_sequence = ['seagreen'])
    st.write(fig1)

elif option == 'Vanguard 500 Index Fund':
    st.subheader('Vanguard 500 Dashboard')
    data_load = st.text('Loading...')
    van_data = yf.download("VFIAX", Start, today)
    data_load.text('Loading Data...Done!')

    van_data.reset_index(inplace=True)

    df1 = van_data[van_data['Date'] == '2017-10-20']
    df2 = van_data[van_data['Date'] == '2018-11-20']
    df3 = van_data[van_data['Date'] == '2019-11-20']
    df4 = van_data[van_data['Date'] == '2020-10-20']
    df5 = van_data[van_data['Date'] == '2021-10-20']
    df6 = van_data[van_data['Date'] == '2022-10-20']

    list_dfs = [df1, df2, df3, df4, df5, df6]
    merged_df = pd.concat(list_dfs)
    merged_df.reset_index(inplace=True)
    merged_df = merged_df.drop(['index'], axis=1)

    st.subheader('Shows the change in price over 5 years')
    st.write(merged_df)
    fig = px.line(van_data['Open'], title='Vanguard 500 Index Fund')
    fig.update_yaxes(title_text='Value ($)')
    fig.update_traces(line_color='purple')
    st.write(fig)

    #Creates a Histogram with the Volume of Trades
    st.subheader('Vanguard 500 Index Fund Volume')
    van_volume = van_data['Volume']
    fig1 = px.histogram(van_volume)
    st.write(fig1)

elif option == 'Schwab S&P 500 Index Fund':
    st.subheader('Schwab S&P 500 Index Fund')
    data_load = st.text('Loading...')
    schwab_data = yf.download("SWPPX", Start, today)
    data_load.text('Loading Data...Done!')

    schwab_data.reset_index(inplace=True)

    df1 = schwab_data[schwab_data['Date'] == '2017-10-20']
    df2 = schwab_data[schwab_data['Date'] == '2018-11-20']
    df3 = schwab_data[schwab_data['Date'] == '2019-11-20']
    df4 = schwab_data[schwab_data['Date'] == '2020-10-20']
    df5 = schwab_data[schwab_data['Date'] == '2021-10-20']
    df6 = schwab_data[schwab_data['Date'] == '2022-10-20']

    list_dfs = [df1, df2, df3, df4, df5, df6]
    merged_df = pd.concat(list_dfs)
    merged_df.reset_index(inplace=True)
    merged_df = merged_df.drop(['index'], axis=1)

    st.subheader('Shows the change in price over 5 years')
    st.write(merged_df)
    fig = px.line(schwab_data['Open'], title='Schwab S&P 500 Index Fund')
    fig.update_yaxes(title_text='Value ($)')
    fig.update_traces(line_color='orange')
    st.write(fig)

    # Creates a Histogram with the Volume of Trades
    st.subheader('Schwab S&P 500 Index Fund Volume')
    schwab_volume = schwab_data['Volume']
    fig1 = px.histogram(schwab_volume)
    st.write(fig1)

elif option == 'Vanguard S&P 500 ETF':
    st.subheader('Vanguard S&P 500 ETF')
    data_load = st.text('Loading...')
    van500_data = yf.download("VOO", Start, today)
    data_load.text('Loading Data...Done!')

    van500_data.reset_index(inplace=True)

    df1 = van500_data[van500_data['Date'] == '2017-10-20']
    df2 = van500_data[van500_data['Date'] == '2018-11-20']
    df3 = van500_data[van500_data['Date'] == '2019-11-20']
    df4 = van500_data[van500_data['Date'] == '2020-10-20']
    df5 = van500_data[van500_data['Date'] == '2021-10-20']
    df6 = van500_data[van500_data['Date'] == '2022-10-20']

    list_dfs = [df1, df2, df3, df4, df5, df6]
    merged_df = pd.concat(list_dfs)
    merged_df.reset_index(inplace=True)
    merged_df = merged_df.drop(['index'], axis=1)

    st.subheader('Shows the change in price over 5 years')
    st.write(merged_df)
    fig = px.line(van500_data['Open'], title='Vanguard S&P 500 ETF')
    fig.update_yaxes(title_text='Value ($)')
    fig.update_traces(line_color='blue')
    st.write(fig)

    # Creates a Histogram with the Volume of Trades
    st.subheader('Vanguard S&P 500 Index Fund Volume')
    van500_volume = van500_data['Volume']
    fig1 = px.histogram(van500_volume)
    st.write(fig1)












