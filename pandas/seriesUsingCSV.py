import numpy as np
import pandas as pd

# Series Using read_csv

##### with 1 column#######

print(type(pd.read_csv(r"C:\Users\NIKHIL\OneDrive\Documents\Desktop\BasicToAd.py\csv_files\subs.csv"))) #type(dataframe)

print(type(pd.read_csv(r"C:\Users\NIKHIL\OneDrive\Documents\Desktop\BasicToAd.py\csv_files\subs.csv",).squeeze("columns")))

subs = pd.read_csv(r"C:\Users\NIKHIL\OneDrive\Documents\Desktop\BasicToAd.py\csv_files\subs.csv").squeeze("columns")

print(subs)

##### with 2 column########f
vk = pd.read_csv(r"C:\Users\NIKHIL\OneDrive\Documents\Desktop\BasicToAd.py\csv_files\kohli_ipl.csv",index_col="match_no").squeeze("columns")
print(vk)

movies = pd.read_csv(r"C:\Users\NIKHIL\OneDrive\Documents\Desktop\BasicToAd.py\csv_files\bollywood.csv",index_col="movie").squeeze("columns")
print(movies)

# Series Methods

####head and tail######
print(movies.head())
print(vk.head(3))
print(vk.tail())
print(subs.tail(10))

#######sample######

print(vk.sample())
print(movies.sample(10))