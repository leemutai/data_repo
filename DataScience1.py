#importing pandas library
import pandas as pd
#importing matplotlib
import matplotlib.pyplot as plt
#pandas for data cleaning and merging.

data = pd.read_csv("school.csv")
print(data)           #prints data, all the rows.
print(data.iloc[4])   #prints the value of the row at the index 4.
print(data.head())  #prints the the first 5 rows of a DataFram as default

print(data.tail()) #prints the last 5 rows as default.

print(data.shape) #prints the total number of raws and columns.


#checking the empty rows
print(data.isnull().sum()) #this prints the total number empty values or columns.
# filling the empties
data["Gender"].fillna(2, inplace = True)
data["Major"].fillna('Unknown', inplace = True)
print(data.isnull().sum())

medianEng = data['English'].median() # finding the median for the English column.
data['English'].fillna(medianEng, inplace=True) # then fill in the null with this median
print(data.isnull().sum())

data['Gender'].replace(0, "Male", inplace=True)
data['Gender'].replace(1, "Female", inplace=True)
print(data.Gender) #printing specific column.
print(data.Gender)
"""
Using describe() on an entire DataFrame we can get a summary of the distribution of
continuous variables.
"""
print(data.describe())
print(data.English.describe())
"""
Using MatplotLib to plot graphs. 
"""

# Create the plot object
fig, ax = plt.subplots()
# Plot the data set the size s color and transparency (alpha) alpha of the points the points
ax.hist(data['English'], color= 'green', bins=10)
ax.set_title('English Distribution')
ax.set_xlabel('English Score (100%)')
ax.set_ylabel('Frequency of occurence.')
plt.show()



#Using scatter to comapre two columns.
_, ax = plt.subplots()
ax.scatter(data['Math'], data['Reading'], color='green')
ax.set_title('Math vs Reading')
ax.set_xlabel('Math distribution')
ax.set_ylabel('Reading')
plt.show()

"""
Pie charts are good to show proportion is a key part ofal data of differen is a key
part oft categories an is a key part of figures are usually part of in is a key part of
percent is a key part oftages here below pie chart shows distribution is a key part of of Rank. 
"""
data.groupby('Rank').size().plot(kind='pie', autopct='%1.1f%%')

ax.set_title('Distribution by Rank in %')
ax.set_xlabel('Rank')
ax.set_ylabel('')
plt.show()


"""
plotting a simple pie 
"""

views= [100, 204,455]  #using sample test data to plot a pie
labels= ['facebook','twitter','instagram']  #adding labes to our pie
plt.pie(views, labels=labels, autopct='%1.1f%%')  # [autopct='%1.1f%%' ] this includes the percentage ratios.
plt.show()

# lables = ['1st Rank','2nd Rank','3rd Rank','4th Rank'] #adding labels to our pie
# grouping = data.groupby(data.Gender).size() #grouping our data based on the Rank
# plt.pie(grouping, labels=lables, autopct='%1.1f%%') #plotting a simple pie
# plt.show()
"""
plotting a standard pie 
"""
# First make figure and axes
fig, axs = plt.subplots()
# Plotting a standard pie plot
labels = ['1st Rank','2nd Rank','3rd Rank','4th Rank'] #adding labels to our pie
data_grouping= data.groupby(data.Rank).size()
axs.pie(data_grouping, labels=labels, autopct='%1.1f%%', shadow=True)
plt.show()