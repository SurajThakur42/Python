try:
  a = int(input("Enter your age : "))
  print("Your age is {a}")

except ValueError as v:
  print(v)
  print("Heyyuyyyy")

except Exception as e:
  print(e)

print("Thanks for co operate")
