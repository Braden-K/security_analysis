import yfinance as yf

class TechnicalIndicator:

    def __init__(self, ticker):
        self.stock_df = yf.download(ticker)
        