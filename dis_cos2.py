# Mark a task as completed

# Show task numbers.
# User enters task number.
# Update its status to completed.

# Concepts:

# Lists
# Indexing
# Conditionals
tasks = []
while True:
    task= input("Enter your task: ")
    subject =input ("Enter subject of your task:")
    status_of_task = False
    new_task = {
    "status_of_task" :status_of_task,
    "task": task ,
    "subject": subject,
    }
    tasks.append(new_task)
    
    ans = input("Do you want to add another task? (yes/no): ").lower()
    if ans =="yes":
        continue
    if ans == "no":
     task_no =int(input("which task do you want to get completed:"))
    for index,task in enumerate(tasks,start =1):
       if (index == task_no):
          print(task_no, "completed")
          task["status_of_task"] = True
          break
    print("\nYour Tasks\n")
    for i, task in enumerate(tasks, start=1):
            print(f"Task {i}")
            print(f"Task Name : {task['task']}")
            print(f"Subject   : {task['subject']}")
            print(f"Status: {task['status_of_task']}")
            print("-" * 25)
          

    