class Employee:
    def __init__(self):
        print("The constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("The constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("The constructor of Manager")
    c = 3

# o = Employee
# print(o.a)
# # print(o.b)

# o = Programmer()
# print(o.a,o.b)

o = Manager()
print(o.a,o.b,o.c)
