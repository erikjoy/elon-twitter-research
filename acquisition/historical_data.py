import yfinance as yf
import pandas as pd

symbol = 'TSLA'

ticker = yf.Ticker(symbol)
hist = ticker.history(period='max')
hist.to_csv('{}_historical.csv'.format(symbol.lower()))