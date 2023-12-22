import yfinance as yf
from utils import fetchDataFrame, fetchStockInfo

class Stock:

    def __init__(self, ticker):
        self.ticker = ticker
        self.df = fetchDataFrame(ticker)
        self.info = fetchStockInfo(ticker)

    def __str__(self):
        print(self.ticker)


   



    
