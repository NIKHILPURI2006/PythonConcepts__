def square(a):
    return a*a

def cube(a):
    return a*a*a

def is_greater(num):
    return num>5

# map func example
func = [square,cube]
for i in range(5):
   val = list(map(lambda x:x(i),func))
   print(val)

# filter  func example
list1 = [4,8,9,6,54,6,5,8]
ans = list(filter(is_greater,list1))
print(ans)