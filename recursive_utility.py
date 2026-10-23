# Challenge 6 — Recursive Utility

# Create a menu:

# 1. Recursive Countdown
# 2. Factorial
# 3. Fibonacci

# Rules:
# • No loops inside recursive functions.

# Concepts:
# • Recursion
# • Base cases
# • Functions

# 🆕 New Concept:
# • Multiple recursive algorithms

# Bonus:
# Count how many recursive calls were made.
calls = 0
def recursive_countdown(number):
   global calls
   calls += 1
   if number == 0 :
      print("Blast off")
      return
   print(number)
   recursive_countdown(number -1)

def factorial(number):
    global calls
    calls += 1
    if number ==0:
       return 1
    else :
       return number*factorial(number-1)

def fibonacci(number):
   global calls 
   calls += 1
   if number == 0:
      return 0
   if number == 1:
      return 1
   else:
       return fibonacci(number-1)+fibonacci(number-2)
       
    
def menu():
    global calls
    while True:
      print("1.Recursive Countdown\n2. Factorial\n3.Fibonacci\n4.Exit")
      try:
       choice= int(input("Enter your choice (1-4):"))
      except ValueError:
         print("Please enter a number between 1 and 4.")
         continue
      if choice == 1:
         number= int(input("Enter number:"))
         calls =0
         if number < 0:
          print("Please enter a non-negative number.")
          continue
         recursive_countdown(number)
         print(f"Calls:{calls}")

      elif choice == 2 :
         number = int(input("Enter number:"))
         calls =0
         if number < 0:
           print("Please enter a non-negative number.")
           continue
         print(factorial(number))
         print(f"Calls:{calls}")

      elif choice == 3 : 
        number =int(input("Enter number:"))
        calls =0
        if number < 0:
         print("Please enter a non-negative number.")
         continue
        print(fibonacci(number))
        print(f"Calls:{calls}")
      
      elif choice == 4:
        break
      else:
       print("Invalid choice. Please enter 1, 2, 3, or 4.")
      
menu()

    

     

