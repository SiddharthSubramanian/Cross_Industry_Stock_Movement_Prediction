# Cross_Industry_Stock_Movement_
Predict change in volatility of stock prices of one industry due to change in other 


In this project , we are going to see the impact of change in volatility of Auto Stocks due to change in Metal Stocks 
The Project uses Seq2Seq LSTM model to use the sequences of price changes in Metal Stocks as an input to Predict changes in Auto Stocks

The Model takes input as changes in Close Price, Delivery of shares for last 14 trading sessions and predicts the expected movement in the Auto Stocks for the 15th day. 

## Architecture of Seq2Seq LSTM Model

![image](https://user-images.githubusercontent.com/7775773/124611781-ad93a980-de69-11eb-869a-05148a82d753.png)



## Architecture of Seq2Seq LSTM Model with Attention


![image](https://user-images.githubusercontent.com/7775773/124639266-e0e33200-de83-11eb-8eec-62ee1ec268e1.png)


## Result

The plain Seq2Seq is successful in predicting the direction of all 13 stocks 61% of time while the attention model is successful by 69% of time
