
try:
    num1 = int(input("enter num 1 : "))
    num2 = int(input("enter num 2 : "))
    print("sum of num1 and num2 is : ",num1+num2)

except Exception as ValueError:
    print("values must be number")