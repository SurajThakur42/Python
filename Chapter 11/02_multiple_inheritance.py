class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class coder():
    location = "Home"
    language = "Python"
    def printlanguage(self):
        print (f"Out of all the languages here i your language : {self.language}")

# class programer(Employee,coder):
#     company = "ITC"
#     def show(self):
#          print(f"The name is {self.name} and the salary is {self.salary}")

#     def showlanguage(self):
#          print(f"The name is {self.name} and the language is {self.language}")


class programmer(Employee,coder):
    salary = "400000000"
a = Employee()
b =programmer()

print(b.location,b.company)
