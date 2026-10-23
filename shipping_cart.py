## Challenge 4 — Shopping Cart
# User enters:
# * Item
# * Price
# * Quantity
# Display:
# * Total bill
# * Number of items
### Concepts
# * Dictionaries
# * Arithmetic
# * Loops
# * Functions

items =[]
def add_item():
 while True:
    item_name = input("Enter name of the item you want to buy:")
    item_qty = int(input(f"How many {item_name} you want to buy: "))
    item_price =int(input(f"Enter price of {item_name}:"))
    item_total = item_price * item_qty
    new_item ={
    "item_name" :item_name,
    "item_qty": item_qty,
    "item_price": item_price,
    "item_total": item_total ,
    }
    items.append(new_item)
  
    add = input("Do you want to add new item?yes/no:").lower()
    if add == "yes":
      continue
    elif add == "no":
      return items

def calculate_total(items):
 total = 0
 for item in items :
     total += item['item_total']
 return total
    
def count_items(items):
  no_of_items = len(items)
  return no_of_items

def most_expensive_item(items):
   check =0
   for item in items :
      if item['item_price'] > check:
         check = item['item_price']
         most_expensive = item

         
   return most_expensive
  

        
def display_items(items):
    print("\nYour Items\n")
    for i, item in enumerate(items, start=1):
            print(f"Item {i}")
            print(f"Item_name : {item['item_name']}")
            print(f"Unit Price: {item['item_price']}")
            print(f"Quantity of item : {item['item_qty']}")
            print(f"Total Price: {item['item_total']}")
            print("-" * 25)

def main():
   items =add_item()
   display_items(items)
   total = calculate_total(items)
   print(f"Bill : {total}") 
   no_of_items =count_items(items) 
   print(f"No_of_items : {no_of_items}")
   print( "_" * 25)
   most_expensive =most_expensive_item(items)
   print ("Information of most expensive item")
   print(f"name: {most_expensive['item_name']}")
   print(f"price: {most_expensive['item_price']}")
   print(f"quantity : {most_expensive['item_qty']}")
   print(f"total_price : {most_expensive['item_total']}")

main() 


