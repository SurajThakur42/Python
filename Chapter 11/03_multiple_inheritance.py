class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee
print(o.a)
# print(o.b)

d = Programmer()
print(d.a,d.b)

e = Manager()
print(e.a,e.b,e.c)
