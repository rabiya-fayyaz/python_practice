
password = input("Enter your password:")

has_digit= False
for character in password:
 if character.isdigit():
  has_digit = True
 
has_upper = False 
for character in password :
 if character.isupper():
   has_upper =True
 
if (len(password) >=6) and has_digit and has_upper   :
    print("Strong")
    
elif (len(password) >=6) and (has_digit or has_upper) :
    print("Medium")
    
else:
    print("Weak")
