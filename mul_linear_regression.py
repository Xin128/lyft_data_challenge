import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn import metrics

###################################################
loc = "/Users/liutianrui/Desktop/0910/main_factors"
dataset = pd.read_csv(loc)

Y = dataset[["career_len"]]
#X = dataset[["rides_per_day","total_duration","profit"]]
X = dataset[["rides_per_day","total_duration","profit","speed","waiting"]]

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=3)

# print (X_train.shape) 200,3
# print (X_test.shape) 87,3
# print (Y_train.shape) 200,1
# print (Y_test.shape) 87,1

regressor = LogisticRegression()
regressor.fit(X_train,Y_train)

# v = pd.DataFrame(regressor.coef_,index=["Co-efficient"]).transpose()
# w = pd.DataFrame(X.columns, columns=["Attribute"])
# coeff_df = pd.concat([w,v], axis=1, join = "inner")
#print (coeff_df)

y_pred = regressor.predict(X_test)
y_pred = pd.DataFrame(y_pred, columns=["Predicted"])
#print (y_pred)

print ("Mean Absolute Error:", metrics.mean_absolute_error(Y_test, y_pred))
print ("Mean Squared Error:", metrics.mean_squared_error(Y_test, y_pred))
print ("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(Y_test, y_pred)))

# t = (pd.Series(Y_test["career_len"]))
# p = (pd.Series(y_pred["Predicted"]))
# print (t)
# print (p)