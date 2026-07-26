import numpy as np

# ============Advanced indexing=============

a1 = np.arange(24).reshape(6,4)
a2 = np.random.randint(1,100,24).reshape(6,4)

print(a1)
print(a2)

#=============== fancy indexing (used when there is no pattern there and normal indexing can't be used)======

print(a1[[0,2,3,5]]) #results in 1st,3rd,4th,6th row

print(a1[:,[0,2,3]]) #results in ist,third,fourth column


# =============Boolean Indexing=================

# find all the no.>50 in a2;
print(a2[a2>50])

# find all the even no.in a2;
print(a2[a2%2 == 0])

# find all the no. in a2 greater than 50 and also even;
print(a2[(a2>50) & (a2%2 == 0)])

# find all the no. not divisble by 7 in a2;
print(a2[a2%7 != 0])