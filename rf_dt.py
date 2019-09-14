import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from math import sqrt


loc = "/Users/liutianrui/Desktop/0910/main_factors"
dataset = pd.read_csv(loc)

Y = dataset[["career_len"]]
X = dataset[["rides_per_day","total_duration","profit","speed"]]

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2, random_state=123)

# print (X_train.shape)
# print (X_test.shape)
# print (Y_train.shape)
# print (Y_test.shape)

scaler = StandardScaler()
train_scaled = scaler.fit_transform(X_train)
test_scaled = scaler.transform(X_test)

tree_model = DecisionTreeRegressor()
rf_model = RandomForestRegressor()

tree_model.fit(train_scaled, y_train)
rf_model.fit(train_scaled, y_train)

# tree_mse = mean_squared_error(y_train, tree_model.predict(train_scaled))
# tree_mae = mean_absolute_error(y_train, tree_model.predict(train_scaled))
# rf_mse = mean_squared_error(y_train, rf_model.predict(train_scaled))
# rf_mae = mean_absolute_error(y_train, rf_model.predict(train_scaled))
#
# print("Decision Tree training mse = ",tree_mse," & mae = ",tree_mae," & rmse = ", sqrt(tree_mse))
# print("Random Forest training mse = ",rf_mse," & mae = ",rf_mae," & rmse = ", sqrt(rf_mse))


tree_test_mse = mean_squared_error(y_test, tree_model.predict(test_scaled))
tree_test_mae = mean_absolute_error(y_test, tree_model.predict(test_scaled))
rf_test_mse = mean_squared_error(y_test, rf_model.predict(test_scaled))
rf_test_mae = mean_absolute_error(y_test, rf_model.predict(test_scaled))

print("Decision Tree test mse = ",tree_test_mse," & mae = ",tree_test_mae," & rmse = ", sqrt(tree_test_mse))
print("Random Forest test mse = ",rf_test_mse," & mae = ",rf_test_mae," & rmse = ", sqrt(rf_test_mse))