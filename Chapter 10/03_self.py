class students():
    language = "C"
    Timeforstudy = "3 hour"      # This is a class attribute.
    location = "Home"

    def getinfo(self):
        print(f"The language is{self.language} and the Time for study is {self.Timeforstudy}.")
    @staticmethod
    def greet():
        print (f"Good morning")

Suraj = students()
Suraj.language = "Python"         # This is a instance attribute.
print(Suraj.Timeforstudy,Suraj.language)

Suraj.getinfo()             # both are same.
students.getinfo(Suraj)

Suraj.greet()
students.greet(Suraj)
