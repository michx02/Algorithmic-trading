"""
Project: Implementing and Backtesting trading strategies using Historical data. 
Strategies: Mean reversion, Momentum trading, Arbitrage


"""

import pandas as pd ## used for data manipulation and analysis
import numpy as np ## for matrices
import matplotlib.pyplot as plt ## for plotting graphs
import yfinance as yf #financial data from Yahoo
from datetime import datetime # for date and time

#download past Stock data
#Ticker (= A code for the name of the stock)

def download_data(ticker,start,end):
    data= yf.download(ticker, start=start, end= end)
    data["Return"] = data["Adj Close"].pct_change()
    data.dropna(inplace=True)
    
    return data




start_date = "2010-01-07"
end_date= datetime.today().strftime('%Y-%m-%d')
ticker= "AAPL"

data= download_data(ticker, start_date, end_date)



def mean_reversion_strategy(data, short_window, long_window):
    data["Short_MA"] = data['Adj Close'].rolling(window=short_window).mean() #MA: Moving Average
    data["Long_MA"] = data["Adj Close"].rolling(window= long_window).mean()
    data["Signal"] = 0
    data["Signal"][short_window:]= np.where(data['Short_MA'][short_window:] > 
                                            data['Long_MA'][short_window:], 1, 0)
    data['Position'] = data['Signal'].diff()

    return data


short_window=10
long_window = 30
data= mean_reversion_strategy(data,short_window,long_window)

plt.figure(figsize=(14,7))
plt.plot(data["Adj Close"],label=f"{ticker} Adj Price") #used f-string for label
plt.plot(data["Short_MA"], label="Short MA")
plt.plot(data["Long_MA"], label="Long MA")
plt.plot(data.loc[data['Position'] == 1].index, 
         data['Short_MA'][data['Position'] == 1], 
         '^', markersize=10, color='g', lw=0,
           label='Buy Signal')

plt.plot(data.loc[data['Position'] == -1].index,
          data['Short_MA'][data['Position'] == -1], 
          'v', markersize=10, color='r', lw=0, 
          label='Sell Signal')

plt.title('Mean Reversion Strategy')

plt.legend() #Display labels
plt.show()



def backtest_strategy(data):
    data['Strategy_Return'] = data['Return'] * data['Signal'].shift(1)
    data['Cumulative_Strategy_Return'] = (1 + data['Strategy_Return']).cumprod()
    data['Cumulative_Market_Return'] = (1 + data['Return']).cumprod()
    return data

data = backtest_strategy(data)
plt.figure(figsize=(14, 7))
plt.plot(data['Cumulative_Strategy_Return'], label='Strategy Return')
plt.plot(data['Cumulative_Market_Return'], label='Market Return')
plt.legend(loc='best')
plt.title('Backtest Results')
plt.show()

