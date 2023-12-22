from technicalIndicator import TechnicalIndicator
from stock import Stock
from typing import Optional
class TrendIndicator(TechnicalIndicator):

    def __init__(self, ticker):
        super().__init__(ticker)


    def simpleMovingAverage(self, 
                            days_preceding: Optional[int] = None,
                            start: Optional[str] = None,
                            end: Optional[str] = None,
                            decimals_rounded_to: Optional[int] = None):
        
        df = self.extract_range(start, end, days_preceding)

        close_sum = df["Close"].sum(axis=0)
        
        if decimals_rounded_to:
            return round(close_sum / len(df.index), decimals_rounded_to)
        return close_sum / len(df.index) 
    

    def expontialMovingAverage(self,
                               days_preceding: Optional[int] = None,
                               start: Optional[str] = None,
                               end: Optional[str] = None,
                               decimals_rounded_to: Optional[int] = None,
                               smoothing_factor: Optional[float] = 0.5):
        
        df = self.extract_range(start, end, days_preceding)

        window_size = len(df.index)
        prices = df["Close"].array
        ema = prices[0]

        for i in range(1, window_size):
            ema = smoothing_factor * prices[i] + (1 - smoothing_factor) * ema

        return ema if not decimals_rounded_to else round(ema, decimals_rounded_to)
    
    








        

        
        


