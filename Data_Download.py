## import required packages
import pandas as pd
import requests
import pickle
from NSEDownload import stocks
from NSEDownload import indices

## get list of stocklisted stocks
Auto = [] ## removed names of stocks temporarily
Metal = [] ## removed names of stocks temporarily

## creating dictionary to store the downloaded data of both sectors
Metal_data = {}
Auto_data = {}

## updating the dictionary with stock data using NSEDownload, getting 3 years data
for l in Auto:
  Auto_data[l] = stocks.get_data(stockSymbol=l, start_date = '01-01-2018', end_date = '03-06-2021')

for m in Metal:
  Metal_data[m] = stocks.get_data(stockSymbol=m, start_date = '01-01-2018', end_date = '03-06-2021')
 
## saving data for future reference

with open('Meta_stocks.pickle', 'wb') as handle:
    pickle.dump(Metal_data, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('Auto_stocks.pickle', 'wb') as handle:
    pickle.dump(Auto_data, handle, protocol=pickle.HIGHEST_PROTOCOL)
