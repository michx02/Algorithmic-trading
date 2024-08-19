import pandas as pd ## used for data manipulation and analysis
import numpy as np ## for matrices
import matplotlib.pyplot as plt ## for plotting graphs
from mrs_strategy import data


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

