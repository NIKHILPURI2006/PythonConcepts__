import numpy as np

a1 = np.random.random((3,3))
a1 = np.round(a1*100)
print(a1)

# ==========max/min/sum/prod=========

print(np.max(a1))
print(np.min(a1))
print(np.sum(a1))
print(np.prod(a1))

print(np.max(a1,axis=0)) #0->columnwise max
print(np.max(a1,axis=1)) #1->rowwise max


print(np.sum(a1,axis=0))#0->col
print(np.sum(a1,axis=1))#1->row

print(np.prod(a1,axis=0)) #0->col


# ===========mean/median/std/var=========(std->standard deviation,var->variance)

print(np.mean(a1,axis=0))
print(np.mean(a1))

print(np.std(a1,axis=1))

print(np.var(a1,axis=0))
print(np.var(a1))

print(np.median(a1))
print(np.median(a1,axis=0))

# ============trignometric functions==============

print(np.sin(a1))

print(np.tan(a1))

print(np.cosh(a1))

# ============dot product of two vectors==========

a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)

print(np.dot(a2,a3))

# ===========log and exponents===============

print(np.log(a1))
print(np.exp(a2))


# ===========round/floor/ceil=================

print(np.round(np.random.random((2,3))*100))#round offs the values 
print(np.floor(np.random.random((2,3))*100))#take to the previous int (ex: if 6.9 is value then it will become 6 )
print(np.ceil(np.random.random((2,3))*100))#takes to th next int (ex: if 6.9 is value then it will become 7 )