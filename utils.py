import yfinance as yf

def fetchDataFrame(ticker):
    return yf.download(ticker)

def fetchStockInfo(ticker):
    return yf.Ticker(ticker).info
