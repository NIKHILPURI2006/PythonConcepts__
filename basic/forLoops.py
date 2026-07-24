list = ["nick","ani","vish"]
list2 = [["a",1],["b",2],["c",3]]
dict = dict(list2)
for j,k in dict.items():
    print(j,"and",k)
for i in list:
    print(i)
items = [int,float,78,9,7,4,3,5,6,]    
for item in items :
    if str(item).isalnum() and item>3:
        print(item)