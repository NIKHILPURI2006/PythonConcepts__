# factorial func..
def factorial(n):
    """
    finding factorial of  given num
    """
    if n == 0:
        return 1
    
    return n*factorial(n-1)
# fiboancci series fucn...
def fibonacci(n):
    """
    finding the fibonacci number of the entered num
    """
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    

num = int(input("enter the number you want factorial of : "))
print(factorial(num))
print(fibonacci(num))