# Question 1
# Create a task and store it.
#
# Requirements:
# - Ask the user for a task name and subject.
# - Store it in a list.
# - Display all tasks.
#
# Concepts:
# - Variables
# - Lists
# - Loops
# - Functions
tasks = []
while True:
    task= input("Enter your task: ")
    subject =input ("Enter subject of your task:")
    new_task = {
    "task": task,
    "subject": subject
}
    tasks.append(new_task)
    
    ans = input("Do you want to add another task? (yes/no): ").lower()

    if ans == "no":
        print("\nYour Tasks:\n")

        for i, task in enumerate(tasks, start=1):
            print(f"Task {i}")
            print(f"Task Name : {task['task']}")
            print(f"Subject   : {task['subject']}")
            print("-" * 25)

        break    
# Status: Completed
# Date: 07-07-2026    


 
  
