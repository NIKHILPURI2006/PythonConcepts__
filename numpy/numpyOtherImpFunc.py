import numpy as np

a1 = np.random.randint(1,100,15)
a2 = np.random.randint(1,100,24).reshape(6,4)

print(a1)
print(a2)


## ======Sorting Func===========

# ==for 1d array==
print(np.sort(a1))#sorting in ascending order
print(np.sort(a1)[::-1])#sorting in descending order

# ==for 2d array==
print(np.sort(a2))#rowwise
print(np.sort(a2,axis=0))#columnwise

##======= Append Func===========

# ==for 1d array==
print(np.append(a1,200))

# ==for 2d array==
print(np.append(a2,np.ones((a2.shape[0],1)),axis=1))
print(np.append(a2,np.random.random((a2.shape[0],1)),axis=1))

## ========Concatenate Func===========

c = np.arange(6).reshape(2,3)
d = np.arange(6,12).reshape(2,3)

# along row
print(np.concatenate((c,d),axis=0))
# alonf columns
print(np.concatenate((c,d),axis=1))

## Unique Func======

e = np.array([1,1,1,1,1,2,22,2,22,333,333,5])

print(np.unique(e))

## ==============Where Fucn==========(return indices of elements based on the condition)

# find the elements>50 in a1
print(np.where(a1>50))
print(np.where(a2>50))

# replace all the values greater than 50 with 0
print(np.where(a1>50,0,a1))
print(np.where(a2>50,0,a2))

## ============argmax func(provides the index of max element )======

print(np.argmax(a1))
print(np.argmax(a2,axis=0))
print(np.argmax(a2,axis=1))

# ============argmin func(provides the index of min element )======
print(np.argmin(a1))
print(np.argmin(a2,axis=0))
print(np.argmin(a2,axis=1))

# ==========cumsum func(for cumulative sum )===================

print(np.cumsum(a1))
print(np.cumsum(a2,axis=0))
print(np.cumsum(a2,axis=1))

# ================cumprod ===============
print(np.cumprod(a1))
print(np.cumprod(a2,axis=0))
print(np.cumprod(a2,axis=1))

# ==============percentile==============
print(np.percentile(a1,100))
print(np.percentile(a1,0))
print(np.percentile(a1,50))

# ============Histogram==========

print(np.histogram(a1,bins=[0,10,20,30,40,50,60,70,80,90,100]))
print(np.histogram(a1,bins=[0,50,100]))

# ================corrcoef==========

salary = np.array([20000,40000,25000,35000,60000])
experience = np.array([1,3,2,4,2])

print(np.corrcoef(salary,experience))