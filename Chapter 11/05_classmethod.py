class Employee():
    a = 3


    @classmethod
    def show(cls):
        print(f"The class value of a {cls.a}")

b = Employee()
b.a = 56

b.show()
