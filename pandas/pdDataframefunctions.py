import numpy as np
import pandas as pd

movies = pd.read_csv(r"C:\Users\NIKHIL\OneDrive\Documents\Desktop\BasicToAd.py\csv_files\movies.csv")
print(movies)

ipl = pd.read_csv(r"C:\Users\NIKHIL\OneDrive\Documents\Desktop\BasicToAd.py\csv_files\ipl-matches.csv")
print(ipl)

# ==============Important Dataframe Functions==========

# 1)astype
print(ipl.info())
ipl['ID'] = ipl['ID'].astype('int32')
print(ipl.info())