from sklearn.linear_model import LinearRegression
import pandas as pd
data = pd.read_csv('advertising.csv')
#first 5 rows
# print(data.head())
#print the total number of rows and columns
# print(data.shape)
#checking for empties
# print(data.isnull().sum())

# print(data.iloc[:,-1])
# print(data.Sales)
# columns= data.columns[0]
# print(columns)
# print(data[columns])
# print(data.iloc[:,0])

# subset= data.columns[1:5]
# print(subset)
# df = pd.DataFrame(data[subset])
# print(df.head())


# print(data.iloc[subset])
# X = subset.iloc[:,-1]
# print(X)
# X= data.iloc[:,:-1].values
# y = data.iloc[:,4].values
# print(X)
# print('printing X done')
# print(y)

X_columns = data.columns[1:4]
print(X_columns)
y_columns= data.columns[4]
print('printing y column')
print(y_columns)
X =data[X_columns.values]
print(X)
y = data[y_columns]
print('printing y')
print(y)

#splitting our data into test and train
from sklearn.model_selection import train_test_split
test,train = train_test_split(data, test_size=.25)
print('printing number of the test dataset')
print(len(test))
print('printing number of the train dataset')
print(len(train))

#initializing our model
model= LinearRegression()
#training
model.fit(train[X_columns], train[y_columns])
print(model)
#predicting
y_predict = model.predict(test[X_columns])
print(y_predict)
print('printing coefficient: ',model.coef_)
print('printing y intercepts: ',model.intercept_)
#testing the accuracy
from sklearn.metrics import r2_score
score= r2_score(y_predict,test[y_columns])
print('printing the nodel accuracy score ')
print(score)

#plotting the regression line
import matplotlib.pyplot as plt
fig, ax= plt.subplots()
ax.scatter(test[y_columns], y_predict, color = "red")
plt.plot(test[y_columns],test[y_columns])
plt.show()