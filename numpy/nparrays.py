import numpy as np


# using array func to create numpy-arrays
a = np.array([1,2,3])

print(a)

print(type(a))

b = np.array([[1,2,3],[4,5,6]])

print(b)

c = np.array([[1,2],[3,4],[5,6],[8,9]])

print(c)

d = np.array([1,2,3],dtype = complex)

print(d)

e = np.array([[1,2],[3,4],[5,6],[8,9]],dtype = bool)

print(e)

f = np.array([[1,2],[3,4],[5,6],[8,9]],dtype = float)

print(f)

#arrange func and reshape func

g = np.arange(1,11) 

print(g)

h = np.arange(1,11).reshape(2,5)

i = np.arange(1,11).reshape(5,2)

arr = c.reshape(2,4)

print(arr)

print(h)

print(i)

# using diff numpy func to create a matrix

j = np.ones((2,5))

k = np.zeros((3,4))

n = np.linspace(-10,10,10,dtype=int)

l = np.random.random((2,4))

m = np.identity(4)

print(m)

print(l)

print(j)

print(k)

print(n)

