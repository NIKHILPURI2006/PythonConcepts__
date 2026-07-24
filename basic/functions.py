def func1(a,b):
    """ This func is used to calculate sum  """
    sum = 0
    sum = a+b
    print("sum of the no.s given is : ",sum)


def func2(a,b):
    """this func is used to calculate avg of the values given"""
    avg = a+b/2
    return avg



print(func1.__doc__)
print(func2.__doc__)
func1(2,56)
print("avg of the nums passed will be : ",func2(56,88))

