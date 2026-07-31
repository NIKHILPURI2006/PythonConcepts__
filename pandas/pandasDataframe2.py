import numpy as np
import pandas as pd

movies = pd.read_csv(r"C:\Users\NIKHIL\OneDrive\Documents\Desktop\BasicToAd.py\csv_files\movies.csv")
print(movies)

ipl = pd.read_csv(r"C:\Users\NIKHIL\OneDrive\Documents\Desktop\BasicToAd.py\csv_files\ipl-matches.csv")
print(ipl)

# ==========Data Filtering===========

# 1)find all the final winners
mask = ipl['MatchNumber'] == 'Final'
newDf = ipl[mask]
print(newDf[['Season','WinningTeam']])

# or

print(ipl[ipl['MatchNumber']=='Final'][['Season','WinningTeam']])

# 2)how many super over finishes have occured
print(ipl[ipl['SuperOver']=='Y'].shape[0])

# 3)how many matches chennaisuperkings won in kolkata
match_kol = ipl[ipl['City']=='Kolkata']
print("matches won by Chennai Super Kings in Kolkata are : ",match_kol[match_kol['WinningTeam']=='Chennai Super Kings'].shape[0])

# or

print("matches won by Chennai Super Kings in Kolkata are : ",ipl[(ipl['City']=='Kolkata') & (ipl['WinningTeam']=='Chennai Super Kings')].shape[0])

# 4)toss winner is match winner in percentage
total_mathes = ipl.shape[0]
when_true = ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]

percentage = when_true/total_mathes * 100

print(percentage,"of times team winning toss is the winning team ")

# 5)movies with imdb higher than 8 and votes>10000
print("movies with imdb higher than 8 and votes>10000 : ",movies[(movies['imdb_rating']>8 )& (movies['imdb_votes']>10000)].shape[0])

# 6)Action movies with imdb rating higher than 7.5
mask1 = movies['genres'].str.split('|').apply(lambda a:'Action' in a)
mask2 = movies['imdb_rating']>7.5
print(movies[mask1 & mask2])

# write a func that can return the track record of two teams

# ==========Adding new cols===========

# completely new
movies['country'] = 'india'
print(movies.head(1))

# from existing ones we can also do this


