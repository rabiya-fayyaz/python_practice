# Level 3 _OOP
# 9)Create a Task class

# class Task:
#     title
#     subject
#     deadline
#     completed

# Concepts:

# Classes
# Objects
# Constructors
# Method
import datetime
import time 
import json
def load_tasks():
 try:
  with open("tasks.json","r")as f :
   data = json.load(f)
   tasks = []
   for item in data:
    task = Task(item["title"], item["subject"],item["deadline"],item["completed"],item["minutes_studied"])
    tasks.append(task)
  return tasks
   
 except FileNotFoundError:
    tasks = []
    return tasks  
   
class Task:
    
    def __init__(self, title, subject,deadline , completed=False, minutes_studied=0):
        self.title = title
        self.subject = subject
        self.completed = completed
        self.deadline = deadline
        self.minutes_studied = minutes_studied
       
    

def add_tasks(tasks):

    while True:
        title = input("Enter task: ")
        subject = input("Enter subject: ")
        deadline = input("Enter deadline of the task:")
        new_task = Task(title, subject,deadline)

        tasks.append(new_task)

        choice = input("Add another?yes/no: ").lower()

        if choice == "no":
            break

    return tasks

def countdown(tasks):
 today = None
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
      today = (datetime.date.today())
      task = tasks[task_no -1]
      task.completed = True
      task.minutes_studied += time_minutes
      print(f"Task {task_no} completed.")     
     elif ask == "no" :
      break
 return tasks,today

def save_study_date(today):
   today =str(today)
   try:
    with open("streak.json","r")as f:
      dates = json.load(f)
   except FileNotFoundError:
      dates = []
   if today not in dates:
         dates.append(today)
   with open("streak.json","w")as f:
      json.dump(dates,f)

def display_streak(today):
 count = 0
 with open("streak.json","r")as f:
      dates = json.load(f)
      while True:
       if str(today) not in dates:
          break
       else: 
        count += 1
        today = today - datetime.timedelta(days=1)
 return count
       
def total_study_time(tasks):
   total = 0
   for task in tasks:
      total += task.minutes_studied
   return total
         
def display_tasks(tasks):     
    print("\nYour Tasks\n")
    for i, task in enumerate(tasks, start=1):
            print(f"Task {i}")
            print(f"Task Name : {task.title}")
            print(f"Subject   : {task.subject}")
            print(f"Deadline :{task.deadline}")
            status = "Completed" if task.completed  else "Pending"
            print(f"Status     : {status}")
            print(f"Minutes_Studied : {task.minutes_studied}")
            print("-" * 25)

def save_tasks(tasks):
 data = []

 for task in tasks:
    dictionary = {
        "title": task.title,
        "subject": task.subject,
        "deadline":task.deadline,
        "completed": task.completed,
        "minutes_studied": task.minutes_studied
    }

    data.append(dictionary)
 with open("tasks.json", "w") as f:
        json.dump(data,f)

def count_completed(tasks):    
 count = 0       
 for task in tasks:  
     if task.completed :  
      count += 1
 return count

def calculate_percentage(completed_tasks,total_tasks):
  percentage =(completed_tasks/total_tasks)*100
  return percentage

def study_statistics(tasks):
 study_stats={}
 for task in tasks:
    if task.subject in study_stats:
       study_stats[task.subject]+= task.minutes_studied
    else:
        study_stats[task.subject] = task.minutes_studied
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
    tasks,today = countdown(tasks)
    if today is not None:
     save_study_date(today)
     count = display_streak(today)
     if count == 1:
      print(f"Current streak: {count} day")
     else:
        print(f"Current streak: {count} days")
    total = total_study_time(tasks)
    hours = total // 60
    minutes = total % 60
    hour_word = "hour" if hours == 1 else "hours"
    minute_word = "minute" if minutes == 1 else "minutes"
    print(f"You studied for {hours} {hour_word} {minutes} {minute_word}")
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
