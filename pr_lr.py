import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
from sklearn.metrics import accuracy_score


loc = "/Users/liutianrui/Desktop/main_factors_new.csv"
dataset = pd.read_csv(loc)

Y = dataset[["career_len"]]
#X = dataset[["rides_per_day","total_duration","profit"]]
#X = dataset[["rides_per_day","total_duration","profit","speed","waiting"]]
X = dataset[["speed","rides_per_day","profit"]]

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2, random_state=123)


#generate a model of polynomial features
poly = PolynomialFeatures(degree=1)

#transform the x data for proper fitting (for single variable type it returns,[1,x,x**2])
X_train = poly.fit_transform(X_train)

#transform the prediction to fit the model type
X_test = poly.fit_transform(X_test)

#here we can remove polynomial orders we don't want
#for instance I'm removing the `x` component
# X_train = np.delete(X_train,(1),axis=1)
# predict_ = np.delete(predict_,(1),axis=1)

regressor = LinearRegression()
#regressor = LogisticRegression()
regressor.fit(X_train,Y_train)

y_pred = regressor.predict(X_test)
y_pred = pd.DataFrame(y_pred, columns=["Predicted"])
#print (y_pred)

print ("Mean Absolute Error:", metrics.mean_absolute_error(Y_test, y_pred))
print ("Mean Squared Error:", metrics.mean_squared_error(Y_test, y_pred))
print ("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(Y_test, y_pred)))
#print ("Accuracy Score:", accuracy_score(Y_train, y_pred))