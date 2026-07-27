import numpy as np
import pandas as pd

marks = [56,78,90,100]
subject = ['maths','english','sst','hindi']

marks1 = pd.Series(marks,index=subject,name="Nikhil's marks")

# =========Series Attributes===========

# size
print(marks1.size)

# dtype
print(marks1.dtype)

# name
print(marks1.name)

# is_unique
print(marks1.is_unique)

# index(gives index values of the series)
print(marks1.index)

# values
print(marks1.values)