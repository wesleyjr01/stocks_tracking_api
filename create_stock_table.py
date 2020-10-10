import pandas as pd

from stocks.models import Stock

df = pd.read_csv("stocks/all_stocks.csv")

for index, row in df.iterrows():
    symbol = row["StockSymbol"]
    company_name = row["CompanyName"]

    try:
        Stock.objects.get(stock_symbol=symbol)
    except:
        stock = Stock(stock_symbol=symbol, company_name=company_name)
        stock.save()