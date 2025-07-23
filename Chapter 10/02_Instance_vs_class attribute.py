class students():
    language = "C"
    Timeforstudy = "3 hour"      # This is a class attribute.
    location = "Home"

Suraj = students()
Suraj.language = "Python"         # This is a instance attribute.
print(Suraj.Timeforstudy,Suraj.language)
