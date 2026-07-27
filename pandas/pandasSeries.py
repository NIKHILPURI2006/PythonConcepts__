import numpy as np
import pandas as pd

# ==========Pandas Series==========

#####Series From Lists##############
# strings
country = ['india','usa','nepal','australia']

print(pd.Series(country))

# integers
runs = [67,89,76,78,0,34]

print(pd.Series(runs))

# custom index
marks = [56,78,90,100]
subject = ['maths','english','sst','hindi']
print(pd.Series(marks,index=subject))

# setting a name

marks = pd.Series(marks,index=subject,name="Nikhil's marks")
print(marks)

###########Series From Dict#################

marks1 = {
    'maths':56,'english':78,'sst':90,'hindi':100
}

print(pd.Series(marks1,name="Nikhil's marks"))