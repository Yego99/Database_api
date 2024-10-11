import pandas as pd
import numpy as np
import sqlite3
import logging


data = pd.read_csv("C:\\Users\\diego\\OneDrive\\Desktop\\my_flask_app\\Coding_Exercise_Sample_Data.csv")

#first make a copy to not coprrupt the original data file
df = data.copy()
#Now some sanity checks

#First 10 rows
'''print(df.head(10))'''

#Last 10 rows
'''print(df.tail(10))'''

#Finding the shape of the data
'''print("There are", df.shape[0], 'rows and', df.shape[1], "columns.")'''

#looking at column data types and null values
'''print(df.info())'''

#statistical summery of of the data
'''print(df.describe().T)'''

#Checking for duplicates
'''print('Number of duplicates in this data set:', df.duplicated().sum())'''

#Everything looks good in terms of data quality and completeness. 
#I just want to turn date into a date data type, rename the csv collumns to match the screen shot, and create a billable amount column

#Let's chage the data type on the copy
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%y')
#Now to check to see if it worked
'''print(df.info())'''

#Let's rename a column so we can match the screen shot
df = df.rename(columns={
    'Project': 'Name',
    })
#Check
'''print(df.head())'''

#And finally add a column to capture 'Billable amount'
df['Billable_amount'] = round(df['Hours'] * df['Billable Rate'],2)
#Check
'''print(df.tail(20))'''

#Columns I want for the data table
selected_columns = df[['Name', 'Client', 'Hours', 'Billable Rate', 'Billable_amount']]

#Now that we have preprocessed the data, lets make our database
conn = sqlite3.connect('timesheet_data.db')

#Create a cursor object to execute SQL queries
cursor = conn.cursor()

#Now lets make the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS timesheets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Client TEXT NOT NULL,
    Hours REAL,
    Billable Rate REAL,
    Billable_amount REAL)''')

# Clear the existing data from the timesheets table before inserting new data and reset the autoincrement sequence
cursor.execute('DELETE FROM timesheets')
cursor.execute('DELETE FROM sqlite_sequence WHERE name="timesheets"')  # Reset the id counter
conn.commit()

selected_columns.to_sql('timesheets', conn, if_exists='replace', index=False)

# Commit the changes and close the connection
conn.commit()
conn.close()

logging.basicConfig(level=logging.INFO)
logging.info("Data loaded successfully.")

