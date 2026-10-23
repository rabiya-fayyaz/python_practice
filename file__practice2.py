total = 0
largest_amount = 0
largest_category = ""
with open ("expense.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        category, amount = line.split()
        amount = int(amount)
        print(f"Category: {category}, Amount: {amount}")
        
        total += amount
        if amount > largest_amount:
            largest_amount = amount
            largest_category = category   
    print(f"Total amount: {total}")    
    print(f"Largest amount: {largest_amount} in category: {largest_category}")
    

