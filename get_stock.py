import pandas as pd
import pandas_profiling
import numpy as np

def get_stock():
    stock = pd.read_excel('./static/xlsx/stock.xlsx')
    stock = stock.fillna(0)
    stock = stock.to_dict("records")
    #print(element.values())
    return stock
