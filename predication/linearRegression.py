import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import  confusion_matrix,accuracy_score
from utils.csvUtils import save_to_csv, load_from_csv
import matplotlib.pyplot as plt



df = load_from_csv('result/TSLA.csv')
print(df.head(5))

df['Date']=pd.to_datetime(df.Date)
df.shape
df.drop('Adj Close',axis=1,inplace=True)
df['Volume']=df['Volume'].astype(float)
df.dtypes

df.isnull().sum()
df.isna().any()

df_new = df[np.isfinite(df).all(1)]

df_new['Open'].plot(figsize=(16,6))

x=df_new[['Open','High','Low','Volume']]
y=df_new['Close']   


x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)
regressor=LinearRegression()
regressor.fit(x_train,y_train)

print(regressor.coef_)

print(regressor.intercept_)
predicted=regressor.predict(x_test)
print(predicted)

dfr=pd.DataFrame({'Actual':y_test,'Predicted':predicted})
dfr.sort_values("Actual",ascending=False)
dfr.sort_values("Predicted",ascending=False)
lst=[i for i in range(0,len(dfr.Actual))]
ak=dfr.head(len(dfr.Actual))
aka=ak.sort_values("Actual")
plt.plot(lst,aka)
plt.xlabel("Time")
plt.ylabel("Stock Closing Price")
plt.title("Actual Closing Price")
plt.show()

lst=[i for i in range(0,len(dfr.Actual))]
aak=ak.sort_values("Predicted")
plt.plot(lst,aak,color="Yellow")
plt.xlabel("Time")
plt.ylabel("Stock Closing Price")
plt.title("Predicted Closing Price")
plt.show()

print(regressor.score(x_test,y_test))
#def linear_regression_analysis(X_train, X_test, y_train, y_test, model):