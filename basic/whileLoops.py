list = [1,45,48,56,23,5,2,52]
i = 0
#  basic
while i<45:
    print(i)
    i = i+1

# for sum of first n num
n = int(input("Enter n: "))

i = 1
sum = 0

while i <= n:
    sum += i
    i += 1

print("Sum =", sum)