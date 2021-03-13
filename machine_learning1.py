import  pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
#Import scikit-learn metrics module for accuracy calculation
from sklearn.metrics import accuracy_score
#import below to help in splitting our dataset into train and test.
from sklearn.model_selection import train_test_split

data = pd.read_csv('bank_updated.csv')

# Label → Creditable or Not Creditable (1 or 0)
# Features → {balance, history, purpose…}
# columns =data.columns
# print(data.shape) #checking number of rows and columns.
#checking for empties
# print(data.isnull().sum())

"""
data transformation
"""

data['job'].replace({'unemployed':0, 'housemaid':1,
                     'management':2,  'technician':3,
                     'blue-collar':4,'entrepreneur':5,
                     'services':6, 'admin.':7,'self-employed':8,
                     'retired':9, 'student':10,'unknown':11}, inplace= True)

data['marital'].replace({ 'married':0, 'single':1,
                          'divorced':2, 'unknown':3}, inplace= True)
data['education'].replace({'primary':0, 'secondary':1,
                           'tertiary':2, 'unknown':3}, inplace= True)

data['default'].replace({'yes':0, 'no':1, 'unknown':2}, inplace= True)
data['housing'].replace({'yes':0, 'no':1, 'unknown':2}, inplace= True)
data['loan'].replace({'yes':0, 'no':1}, inplace= True)


"""
splitting our dataset into train and test 
"""
#setting 75% of our data to be train and the 25% for testing
#Splitting dataset into 2 helps in calculating the accuracy of our training model.

train, test = train_test_split(data, test_size=0.2)
print('number of test ',len(test))

print('number of train ',len(train))
# print(train[X].head()) #testing our data splitting by printing for train and test separate

# print('printing X variable for the test dataset')
# print(test[X].head()) #testing our data splitting

"""
defining input and output/target variables
"""
# we take columns default, balance and housing
# to determine loan eligibility (columns at index 0 to 6)
column_subset= data.columns[0:7] #defining variable column's name
# print('columns- subset ')
# print(column_subset)
X= column_subset
target_variable = train['loan'] #loan is the target varible (column index 7)
# print('printing target_variable y')
# print(target_variable)
y=target_variable
# print(y)

"""
training and fitting our model
"""
clf =RandomForestClassifier(n_jobs=2,random_state=0)
#fitting model to our training dataset
clf.fit(train[X], y)
# print(clf)
prediction= clf.predict(test[X])
# print('printing our test dataset')
# print(test['loan'].head(24))#testing for accuracy
# print('printing our predictions')
print(prediction[0:25])

"""
Viewing predicted prababilities of the first 15 rows.
"""
proba_predictions= clf.predict_proba(test[X])[0:15]
print(proba_predictions)
accuracy= accuracy_score(prediction,test['loan'])
print('printing accuracy')
print(accuracy*100)


predict_report=classification_report(test['loan'], prediction)
print('printing predict report')
print(predict_report)