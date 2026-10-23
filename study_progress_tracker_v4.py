# 4)Study timer

# User enters study minutes.
# Program counts down and announces completion.

# Concepts:

# Loops
# Time module
# Functions
import time 
def add_tasks():
 tasks =[]
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

    if ans =="no": 
        return tasks

def countdown(tasks):
 while True:
  task_no = input("Which task do you want to do?:")
  if task_no == ""  :
    print("no task completed")
    break
  # Handle non-numeric input without crashing the program.
  try:
    task_no = int(task_no)
  except ValueError:
     print("invalid")
     print("Enter valid value")   
     continue
  if task_no < 1 or task_no > len(tasks) :
    print("invalid")
    print("Enter valid value")
  else: 
     study_time =int(input("Enter time for the task in min :")) 
     study_time = study_time * 60 
     for i in range(study_time):
        time.sleep(1)
        study_time -= 1
        minutes = study_time // 60
        seconds = study_time % 60
        print(f"{minutes:02}:{seconds:02}")
     print("Study session finished!")
     ask = input("Have you completed your task?yes/no:").lower()
     if ask == "yes":
      for index,task in enumerate(tasks,start =1):
           if index == task_no:
              print(f"Task {task_no} completed.")
              task["status_of_task"] = True
     elif ask == "no" :
      break
 return tasks 
         
def display_tasks(tasks):     
    print("\nYour Tasks\n")
    for i, task in enumerate(tasks, start=1):
            print(f"Task {i}")
            print(f"Task Name : {task['task']}")
            print(f"Subject   : {task['subject']}")
            status = "Completed" if task["status_of_task"] else "Pending"
            print(f"Status     : {status}")
            print("-" * 25)
   
def count_completed(tasks):    
 count = 0       
 for task in tasks:  
     if task['status_of_task']==True :  
      count += 1
 return count

def calculate_percentage(completed_tasks,total_tasks):
  percentage =(completed_tasks/total_tasks)*100
  return percentage

def main():
    tasks = add_tasks()
    countdown(tasks)
    display_tasks(tasks)
    completed_tasks = count_completed(tasks)
    percentage = calculate_percentage(completed_tasks,len(tasks))
    print(f"{percentage}% completed")
    print(f"{completed_tasks } out of {len(tasks)} tasks completed")

main()


          

    