# Question 3. Install an external module and use it to perform an operation of your interest. 


# pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()
engine.say("hello")
engine.runAndWait()

# pip install pyjokes
import pyjokes
jokes = pyjokes.get_joke()
print (jokes)
