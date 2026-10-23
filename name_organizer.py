# Challenge 7 — Name Organizer
# User enters many names.
# Program should:

# • Remove duplicates
# • Sort alphabetically
# • Search for a name

def get_names():
 names =[]
 while True:
     name =input ("Enter name:").lower()
     names.append(name)
    
     choice =input("Do you want to add another name?yes/no:").lower()
     if choice == "yes":
        continue
     else :
        break
 return names 

def remove_duplicates(names):
   unique = list(set(names))
   return unique

def sort_names(names):
   sorted_names = sorted(names)
   sorted_by_length =sorted(names,key = len)
   return sorted_names,sorted_by_length

def search_names(names):
   search = input("Enter the name you want to search:").lower()
   if search in names:
      print("Found")
   else:
      print("Not found") 

def main():
   names = get_names()
   print("\nOriginal names:")
   print(names)

   unique = remove_duplicates(names)
   print("\nWithout duplicates:")
   print(unique)

   sorted_names,sorted_by_length = sort_names(unique)
   print("\nAlphabetical:")
   print(sorted_names)

   print("\nBy length:")
   print(sorted_by_length)
   
   search_names(sorted_names)

main()


    