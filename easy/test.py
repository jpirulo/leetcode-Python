import yfinance as yf
import datetime as dt

start = dt.datetime(2020,1,1)
end = dt.datetime.now()

eth = yf.download('ETH', start, end)



#!pip install pandas_datareader
import pandas_datareader as web
import datetime as dt

start = dt.datetime(2020,1,1)
end = dt.datetime.now()

ltc = web.DataReader('LTC-USD', 'yahoo', start, end)






#Source: https://stackoverflow.com/questions/71023401



