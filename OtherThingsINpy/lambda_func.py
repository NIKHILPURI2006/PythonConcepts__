# lambda functions
def minusfunc(x,y):
    return x-y

# return the same ans as the above func

minus = lambda x,y : x-y

print(minus(9,5))
print(minusfunc(9,5))

z = [[1,14],[77,23],[5,85]]
z.sort(key=lambda z:z[0])
print(z)