
# 1
print("answers for program ist ")
l = 30
def func1(n):
    l = 90
    m = 84
    print("due to local variable scope value of l is : ",l)
    print("value of m due to local variable : ",m)
    print("i have printed")
func1("i have printed")

# print(m) // it will show error cause m is not defined globally


#  
print("due to global scope of varible l its value is : ",l)


# 2
print("answers for program 2nd")
x = 89
def func1():
    x = 20 
    def func2():
        global x 
        x = 88
    print("before calling func2 value of x : ", x )
    func2()
    print("after calling fucn2 value of x : ", x )
func1()
print("after calling func1 value of x is : ", x )        
