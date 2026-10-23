# 7)Generate study statistics
# Example output:

# Biology: 3 hours
# Chemistry: 5 hours
# Physics: 2 hours
# Most studied subject: Chemistry

# Concepts:

# Dictionaries
# Loops
# Searching for maximum values
import time 
import json
def load_tasks():
 try:
  with open("tasks.json","r")as f :
   tasks = json.load(f)   
   return tasks
   
 except FileNotFoundError:
    tasks = []
    return tasks  
   
def add_tasks(tasks):
 while True:
    task= input("Enter your task: ")
    subject =input ("Enter subject of your task:")
    status_of_task = False
    new_task = {
    "status_of_task" :status_of_task,
    "task": task ,
    "subject": subject,
    "minutes_studied": 0,
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
     time_minutes = study_time
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
              task["minutes_studied"] += time_minutes
     elif ask == "no" :
      break
 return tasks 
def total_study_time(tasks):
   total = 0
   for task in tasks:
      total += task['minutes_studied']
   return total
         
def display_tasks(tasks):     
    print("\nYour Tasks\n")
    for i, task in enumerate(tasks, start=1):
            print(f"Task {i}")
            print(f"Task Name : {task['task']}")
            print(f"Subject   : {task['subject']}")
            status = "Completed" if task["status_of_task"] else "Pending"
            print(f"Status     : {status}")
            print(f"Minutes_Studied : {task['minutes_studied']}")
            print("-" * 25)

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks,f)

def count_completed(tasks):    
 count = 0       
 for task in tasks:  
     if task['status_of_task']==True :  
      count += 1
 return count

def calculate_percentage(completed_tasks,total_tasks):
  percentage =(completed_tasks/total_tasks)*100
  return percentage

def study_statistics(tasks):
 study_stats={}
 for task in tasks:
    if task["subject"] in study_stats:
       study_stats[task['subject']] += task["minutes_studied"]
    else:
        study_stats[task["subject"]] = task["minutes_studied"]
 return study_stats

def most_studied_subject(study_stats):
  highest_minutes = 0
  best_subject= ""
  for subject in study_stats:
    if highest_minutes < study_stats[subject]:
        highest_minutes =  study_stats[subject]
        best_subject = subject
  return highest_minutes,best_subject

def main():
    tasks = load_tasks()
    tasks = add_tasks(tasks)
    countdown(tasks)
    total = total_study_time(tasks)
    hours = total // 60
    minutes = total % 60
    print(f"You studied for {hours} hours {minutes}minutes")
    display_tasks(tasks)
    save_tasks(tasks)
    completed_tasks = count_completed(tasks)
    percentage = calculate_percentage(completed_tasks,len(tasks))
    print(f"{percentage:.2f}% completed")
    print(f"{completed_tasks } out of {len(tasks)} tasks completed")
    study_stats = study_statistics(tasks)
    for subject in study_stats :
     highest_minutes = study_stats[subject]
     studying_hours = highest_minutes// 60
     studying_minutes = highest_minutes % 60
     print(f"{subject}: {studying_hours} hours {studying_minutes} minutes")
    highest_minutes, best_subject = most_studied_subject(study_stats)
    best_hours = highest_minutes// 60
    best_minutes = highest_minutes % 60
    print(f"Most studied subject: {best_subject} ({best_hours} hours {best_minutes} minutes)")
main()
