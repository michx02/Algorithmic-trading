"""
Project: Implementing and Backtesting trading strategies using Historical data. 
Strategies: Mean reversion


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







