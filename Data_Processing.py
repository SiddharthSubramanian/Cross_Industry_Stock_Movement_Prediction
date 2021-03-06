## importing required packages

from datetime import datetime, timedelta
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like #For solving import pandas_datareader issue
import numpy as np
import datetime
import csv

##reading pickle file
with open('Auto_data.pickle', 'rb') as handle:
    Auto_data = pickle.load(handle)
with open('Metal_data.pickle', 'rb') as handle:
    Metal_data = pickle.load(handle)

##inital data processing
    
def data_processing(dict_data_in,dict_data_out):
  input_data = {}
  output_data = {}
  for k in dict_data_in.keys():
    dict_data_in[k].index = pd.to_datetime(dict_data_in[k].index)
    dict_data_in[k].sort_index(inplace=True)
    change_in_price =  (dict_data_in[k]['Close Price'] - dict_data_in[k]['Prev Close'] )/dict_data_in[k]['Prev Close'] 
    change_in_delivery = dict_data_in[k]['Deliverable Qty'].pct_change()
    change_in_delivery[0] = 0
    temp_data = pd.concat([change_in_delivery,change_in_price],axis=1)
    temp_data.columns = ['%_change_delivery','%_change_price']
    input_data[k] = pd.DataFrame(temp_data)
  
  for k in dict_data_out.keys():
    dict_data_out[k].index = pd.to_datetime(dict_data_out[k].index)
    dict_data_out[k].sort_index(inplace=True)
    change_in_price =  (dict_data_out[k]['Close Price'] - dict_data_out[k]['Prev Close'] )/dict_data_out[k]['Prev Close'] 
    change_in_delivery = dict_data_out[k]['Deliverable Qty'].pct_change()
    change_in_delivery[0] = 0
    temp_data_2 = pd.concat([change_in_delivery,change_in_price],axis=1)
    temp_data_2.columns = ['%_change_delivery','%_change_price']
    output_data[k] = pd.DataFrame(temp_data_2)
  return input_data,output_data 

## transforming the data for 1st step
in_data,out_data = data_processing(Metal_data ,Auto_data)

X = pd.DataFrame()
for k in in_data.keys():
  X[k + "_%_change_delivery"] = in_data[k]['%_change_delivery']
  X[k + "_%_change_price"] = in_data[k]['%_change_price']

Y = pd.DataFrame()
for k in out_data.keys():
  Y[k + "_%_change_price"] = out_data[k]['%_change_price']
timestep = 14
X_data = []
Y_data = []
for i in range(len(X)- timestep -1):
    X_data.append(X.iloc[i:(i+timestep)])
    Y_data.append(np.array(Y.iloc[i+timestep]))
split = int(np.ceil(len(X_data)*0.8))
train_X, train_Y = X_data[:split],Y_data[:split]
test_X, test_Y = X_data[split:],Y_data[split:]
train_X = np.array(train_X)
train_Y = np.array(train_Y)

test_X = np.array(test_X)
test_Y = np.array(test_Y)
train_Y = train_Y.reshape(665,1,13)
test_Y = test_Y.reshape(166,1,13)
