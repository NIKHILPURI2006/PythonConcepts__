# first inheritance program
class Employee :
    no_of_leaves = 9
    def __init__(self,aname,asalalry,arole):
         self.name = aname
         self.salary = asalalry
         self.role = arole


    @classmethod
    def change_leaves(cls,newleaves) :
         cls.no_of_leaves = newleaves

# inherits Employee objects also
class Programmer(Employee) :
    def __init__(self,aname,asalalry,arole,aage):
         self.age = aage
    
    def printprog(self):
         return f"name of programmer is {self.name} and salary is {self.salary}"   

nikhil = Employee("Nikhil",75000,"SDE")     

vishal = Employee("Vishal",80000,"Marketing head")

shivang = Programmer("Shivang",90000,"programmer",26)

print(nikhil.role)

print(vishal.salary)

print(shivang.age)