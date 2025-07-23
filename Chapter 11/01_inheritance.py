class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class programer:
#     company = "ITC"
#     def show(self):
#          print(f"The name is {self.name} and the salary is {self.salary}")

#     def showlanguage(self):
#          print(f"The name is {self.name} and the language is {self.language}")


class programmer(Employee):
    name = "Suraj"
a = Employee()
b =programmer()

print(a.company,b.company)

