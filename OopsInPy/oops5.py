#  first multiple inheritance program
class Employee :
    no_of_leaves = 9
    def __init__(self,name,salalry,role):
         self.name = name
         self.salary = salalry
         self.role = role

    def printdetails(self):
        print(f"name is {self.name},salary is {self.salary} and role is {self.role} ")     

class Player:
     def __init__(self,game,language):
        self.game  = game
        self.language = language

     def printdetails(self):
         print(f"game is {self.game} and language is {self.language}")    

# multiple inherited class
class Coolprogrammer(Employee,Player):
    pass

vishal = Employee("Vishal",80000,"Marketing head")

jai = Player("golf","C++")

vishal.printdetails()
jai.printdetails()