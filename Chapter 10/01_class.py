class Employee:                  
    language = "Py"            # This is a class attribute.
    salary = 1200000

Suraj = Employee()
Suraj.name = "Suraj"
print (Suraj.name,Suraj.language and Suraj.salary)            # This is a instance (object) attribute.
# Here Suraj is a instance (object).               

Rohan = Employee()
Rohan.name = "Rohan"
print (Rohan.name,Rohan.language,Rohan.salary)                  # This is a instance (object) attribute.
#Rohan is a instance (object) here

# Here name is instance (object) attribute and language and salary are class attribute bcoz they directly belong to class.
