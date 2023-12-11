import pandas as pd
import numpy as np
import datetime as dt
import yahoofinancials as yf



tickers = ['MSFT','AAPL']

start_date= dt.date.today().strftime('%Y-%m-%d')
end_date = (dt.date.today() - dt.timedelta(days = 5*365)).strftime('%Y-%m-%d')
for ticker in tickers:
    yf.YahooFinancials(ticker).get_historical_price_data( )