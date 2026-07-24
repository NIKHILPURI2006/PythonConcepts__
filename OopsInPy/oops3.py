class Employee :
    no_of_leaves = 9
    def __init__(self,aname,asalalry,arole):
         self.name = aname
         self.salary = asalalry
         self.role = arole


    @classmethod
    def change_leaves(cls,newleaves) :
         cls.no_of_leaves = newleaves

     
nikhil = Employee("Nikhil",75000,"SDE")     

vishal = Employee("Vishal",80000,"Marketing head")

print(nikhil.role)

print(vishal.salary)

Employee.change_leaves(25)

print(vishal.no_of_leaves)
