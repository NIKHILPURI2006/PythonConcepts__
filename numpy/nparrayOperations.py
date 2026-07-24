import numpy as np

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

# ======Scalar Operations(operates on single array)==========

## sum with scalar
sum = a1 + 7
print(sum)

## prod with scalar
prod = a1 * 3
print(prod)

## div with scalar
div = a1 / 2
print(div)

## exponential with scalar
exp = a1**2
print(exp)

# ==========Relational Operations=========

r1 = (a1>7)
r2 = (a1==12)

print(r1)
print(r2)

# ==========Vector Operations(operates on two arrays) //shape of the arrays must be same===========

v1 = a1**a2
v2 = a1/a2
print(v1)
print(v2)