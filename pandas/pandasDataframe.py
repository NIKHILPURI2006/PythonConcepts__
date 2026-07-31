import numpy as np
import pandas as pd

# ======Pandas Dataframe==========

# using lists 
student_data = [
    [100,56,12],
    [94,58,14],
    [88,64,20]
]
print(pd.DataFrame(student_data,columns=['iq','marks','package']))

# using dicts
student_data1 = {
    'iq':[100,94,88],
    'marks':[56,58,64],
    'package':[12,14,20]
}
student = pd.DataFrame(student_data1)
print(pd.DataFrame(student_data1))

# using read_csv

movies = pd.read_csv(r"C:\Users\NIKHIL\OneDrive\Documents\Desktop\BasicToAd.py\csv_files\movies.csv")
print(movies)

ipl = pd.read_csv(r"C:\Users\NIKHIL\OneDrive\Documents\Desktop\BasicToAd.py\csv_files\ipl-matches.csv")
print(ipl)

# ========Dataframe Attributes and Methods==========

# shape
print(ipl.shape)
print(movies.shape)

# dtypes
print(ipl.dtypes)
print(movies.dtypes)

# index
print(ipl.index)
print(movies.index)

# columns
print(ipl.columns)

# values
print(ipl.values)

# head and tail
print(movies.head(2))
print(ipl.tail(7))

# sample
print(ipl.sample())

# info
print(movies.info())

# describe
print(movies.describe())

# isnull
print(movies.isnull().sum())

# duplicated
print(movies.duplicated().sum())

# rename
student.rename(columns={'package':'lpa'},inplace=True)
print(student)

# ===========Selecting columns from a dataframe==========

# single cols
print(ipl['Venue'])
print(movies['imdb_id'])

# multiple cols
print(movies[['title_x','actors','year_of_release']])
print(ipl[['Team1','Team2','WinningTeam']])

# ==========Selecting rows from a dataframe===============

# using iloc (for single column)
print(movies.iloc[5])

# using iloc (for multiple cols)
print(movies.iloc[[0,4,5]])
print(movies.iloc[5:16])

# using loc 
# same as iloc only takes index value rather than its position

# ============Selecting both rows and cols==============
print(movies.iloc[0:3,0:3])

