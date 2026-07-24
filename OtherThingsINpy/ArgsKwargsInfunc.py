# usinf *args and **kwargs in function arguements
def func1(normal,*args,**kwargs):
    print(f"this is the normal arguement passed in the func : {normal}  ")
    print("\n these are the *args values passed")
    for i in args:
        print(i)
    print("\n these are the kwargs value passed")
    for j,k in kwargs.items():
        print(f"the key is {j} and the value is {k}")

args1 = [1,5,6,8,90]
kwargs1 = {"name":"nikhil","class":"10th","roll no." :"45"}
func1("hey its me",*args1,**kwargs1)