class students():
    language = "C"
    Timeforstudy = "3 hour"      # This is a class attribute.
    location = "Home"

    def __init__(self,name,language,Timeforstudy):  # Dunder method(_init_) which call itself automaticallywhen object is created.
        self.name = name
        self.language = language
        self.Timeforstudy = Timeforstudy
        print("I am creating a object")

    def getinfo(self):
        print(f"The language is{self.language} and the Time for study is {self.Timeforstudy}.")
    @staticmethod
    def greet():
        print (f"Good morning")

Suraj = students("Suraj","Python",3)
Suraj.language = "Python"         # This is a instance attribute.
print(Suraj.Timeforstudy,Suraj.language)


Rohan = students("Rohan","Javascript",5)
Rohan.language = "Java"
print(Rohan.language,Rohan.Timeforstudy)

