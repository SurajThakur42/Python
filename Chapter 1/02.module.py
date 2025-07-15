# MODULE : Module is a file containing code written by someone else which can be use in our programs.
'''PIP : Pip is the package manager for python. By pip we can install module on our system.
In terminal we can download module with the help of pip. '''

# Pip install pyjokes
import pyjokes
print("printing jokes.....")
 
joke = pyjokes.get_joke()
print(joke)

#pip install pyttsx3
import pyttsx3
import pyttsx3
engine = pyttsx3.init()
engine.say("I am starting all program please don't shy to grab a cup of coffee")
engine.runAndWait()


'''Modules is of two types :-
1) Built in Modules(Preinstalled in python)
2) External Modules(Need to install using pip)'''

'''Python as a calculator:-
By entering python in terminal we can do mathematical calculation in terminal.'''

'''Comments:- Comments are used to write something which the programmer does not want to execute.
Comments are of two types :-
1) Single line comments:- Used to comment only one line. We can comment a line using # or ctrl+/.
2) Multiline comments :-  Used to comment multiple lines.We can comment multiple line using('''''').'''
