from typing import Optional
import pandas as pd
from stock import Stock

class TechnicalIndicator:

    def __init__(self, ticker):
        self.stock = Stock(ticker)
          

    def extract_range(self, 
                      start: Optional[str] = None, 
                      end: Optional[str] = None, 
                      days_preceding: Optional[int] = None):

        if not days_preceding and (not start or not end):
            raise ValueError("days_preceding or both start and end must be non-null")
        
        if not days_preceding:
            return self.stock.df[start : end]
        else:
            return self.stock.df[-days_preceding:]


