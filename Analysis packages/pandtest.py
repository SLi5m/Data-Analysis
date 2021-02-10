# Import pandas
import pandas as pd

# Using python dictionary prepare the data
data = {'Name' : ['Bill', 'Dan', 'Tony', 'Mark'],
        'Age' : [28, 29, 31, 27],
        'Salary' : [2000, 2500, 2100, 2200]}

obj = pd.DataFrame(data)

print (obj) # Prints the dataframe in tabular form
print (obj['Age']) # Prints the specific column
print (obj.Age)
print (obj.columns) # Prints the columns of the data frame
print (obj.values) # Returns a the data as a 2D array
print (obj.drop(1)) # Drops a specific row
print (obj.drop('Age', axis=1))


# INDEXING AND SELECTION
# Gives specific indexing to your row
data = pd.DataFrame(data, index=['emp1', 'emp2', 'emp3', 'emp4'])
print (data)

# Indexing format
# data[rows, columns]

# 1. Column selection
# If we know the column name
print (data[['Age', 'Name']])
print (data.loc[:, ['Age', 'Name']])
# ?print (data.ix[:, ['Age', 'Name']])?

# If we don't know the column name
print (data.iloc[:, [0, 1]])

# 2. Row selection
# If we know the index name
# prints indexes 0, 1, 2
print (data.loc['emp1': 'emp3', :])

# If we don't know the index name
# Prints indexes 0 and 1, excludes the last index
print (data.iloc[0:2, :])

# Mixed selection
print (data.loc['emp1':'emp3', ['Name', 'Age']])
print (data.iloc[[0, 2, 3], [0, 2]]) # prints row number 0, 2, 3 and column number 0 and 2

# Filtering data
# prints name and salary of those employees whose age is greater than 28
print (data.loc[data.Age > 28, ['Name', 'Salary']])


# Descriptive statistics

print (data.describe()) # Prints multiple statistics
print ("Mean of salaries is " + str(data.loc[:,'Salary'].mean())) # Prints the mean of salaries
print ("Minimum age of employees is " + str(data.loc[:,'Age'].min())) # Prints minimum age of employees

# Handling missing data
data = pd.DataFrame([[2.3, 3.3, None], [7.5, None, 9.8], [None, 2.2, 6.8], [5.6, 9.2, 7.4], [None, None, None]])
print (data)

# 1. Filtering missing data
print (data.dropna()) # Drop any rows with all null values
print (data.dropna(how='all'))# Drop rows with all null values
print ("This is the mean ////////////////////////////" + str(data.mean()))
# 2. Filling missing data
print (data.fillna(0))  # Fill null values with 0
print (data.fillna(data.mean())) # Fill null values with the mean
print (data.fillna({0:2.5, 1:3.0, 2:5.5})) # Null values for specific columns


# Reading and writing files

data = pd.read_csv('data.csv') # Reads csv file
print (data.head) # print the top 5 rows
pd.DataFrame(data).to_csv('myfile.csv')  # Saves a dataframe to a csv file