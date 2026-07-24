class Student :
    no_of_sick_leaves = 9
    pass

nikhil = Student()

rajan = Student()

nikhil.roll = 40
rajan.roll = 45
nikhil.std = "8th"
rajan.std = "5th"


Student.no_of_sick_leaves = 4
rajan.no_of_sick_leaves = 8

print(Student.__dict__)

print(nikhil.roll,rajan.std)
print(nikhil.std,rajan.roll)
print(nikhil.no_of_sick_leaves)
print(rajan.no_of_sick_leaves)

print(rajan.__dict__)
print(nikhil.__dict__)

print(Student.__dict__)