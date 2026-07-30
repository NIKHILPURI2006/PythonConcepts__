import numpy as np
import pandas as pd


# 1)/////Series Using read_csv


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


# 2)//////Series Methods


####head and tail######
print(movies.head())
print(vk.head(3))
print(vk.tail())
print(subs.tail(10))

#######sample######

print(vk.sample())
print(movies.sample(10))

#######value-counts->movie##########
print(movies.value_counts())

########sort values##############
print(vk.sort_values(ascending=False).head(1).values[0])

#########inplace##########
# vk.sort_values(inplace=True)
# print(vk) #(inplace changes the original vk series not in the temp)

########sort_index########
print(movies.sort_index(ascending=False))


# 3)//////Series Math methods

#########count##############
print(vk.count())

#########sum,product##########
print(subs.sum())
print(subs.product())

########mean->median->mode->std->var########
print(subs.mean())
print(vk.median())
print(movies.mode())
print(subs.std())
print(vk.var())

############min->max########
print(subs.min())
print(subs.max())

######describe########
print(vk.describe())


# 4)//////Series indexing
x = pd.Series([16,45,21,3,2,54,12,78,99])
print(x[0])

print(movies['Uri: The Surgical Strike'])
print(vk[1])


# 5)//////////Series slicing
print(vk[5:16])
print(vk[-5:])
print(movies[::2])


# 6)///////Fancy indexing
print(vk[[1,3,4,5]])


# 7)/////////Series editing
x[1] = 100
print(x)

