D1 = {}
D2 = {"morning" : "breakfast","afternoon":"lunch","night":"dinner"}
print(D2)
D2["latemorning"] = "brunch"
print(D2)
del D2["afternoon"] 
print(D2["morning"])
D3 = D2.copy()
print(D3)
del D3["night"]
D3.update({"evening":"snacks"})
print(D3)
print(D2.keys())
print(D3.keys())
print(D2.items())
print(D3.items())
dict = {"nick":"89",
        "vish":"23",
        "ani":"78"}
name = input("enter name : ")
print(dict[name])
