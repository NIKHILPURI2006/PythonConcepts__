import numpy as np

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)
a4 = np.arange(27).reshape(3,3,3)

print(a1)
print(a2)
print(a3)
print(a4)
# =================Indexing=================

# indexing 1d array
print(a1[0]) #ans is 0
print(a1[-1]) #ans is 9

# indexing of 2d array
print(a2[2,3]) #ans is 11
print(a2[1,2]) #ans is 6

# indexing in 3d array

print(a3[1,0,1]) #ans is 5
print(a3[0,1,0]) #ans is 2
print((a3[0,0,0])) #ans is 0


# ================Slicing====================

#  Slicing in 1d array
print(a1[2:5]) #ans is [2,3,4]

print(a1[2:5:2]) #ans is [2 4]

# Slicing in 2d array

print(a2[0,:]) # gets the first row of a2

print(a2[:,2]) # gets the third columns 

print(a2[1:,1:3]) # ans is [[ 5  6]
 #                           [ 9 10]]


print(a2[::2,::3]) # ans would be [[ 0  3]
#                                   [ 8 11]]

print(a2[::2,1::2]) # ans would be  [[ 1  3]
#                                   [ 9 11]]


# Slicing in 3d array 

print(a4[1,:,:]) 
print(a4[1])   # both give the same result the whole middle 2d array of 'a4'

print(a4[0::2]) # results the first and  last 2d array of 'a4'

print(a4[0,1,:]) # second row of first 2d array of 'a4'

print(a4[0::2,0,0::2]) # ans would be 1st and last element of first row of 1st and second  2d array in a4