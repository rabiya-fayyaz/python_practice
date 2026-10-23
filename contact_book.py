# Allow the user to:

# * Add contacts
# * Display contacts
# * Search contacts

# Each contact should contain:

# * Name
# * Phone Number

def add_contacts():
 contacts =[]
 while True:
    name = input("Enter your contact_no name: ")
    contact_number =input ("Enter contact_number:")
    new_contact = {
    "name": name ,
    "contact_number": contact_number,
    }
    contacts.append(new_contact)
    choice = input("Do you want to add another contact? (yes/no): ").lower()
    if choice =="yes":
     continue
    if choice =="no":
      return contacts 
    break
 
def display_contacts(contacts):
    print("\nYour Contacts:\n")
    for i, contact in enumerate(contacts,start=1):
            print(f"contact {i}")
            print(f"name : {contact['name']}")
            print(f"contact_number  : {contact['contact_number']}")
            print("-" * 25)

def search_contact(contacts):
   while True:
    search_choice = input("Do you want to search for a contact?yes/no:") 
    if search_choice =="yes":
      search_name =input("Enter name of the contact you want to search:").lower()
      contact_found = False
      for contact in contacts:
         if search_name ==  contact['name']:
            contact_found = True
            print(f"name : {contact['name']}")
            print(f"contact_number  : {contact['contact_number']}")
            break
    if contact_found == False:
            print("contact not found")

    if search_choice == "no":
       break

def main():
    contacts= add_contacts()
    display_contacts(contacts)
    search_contact(contacts)
main()

