# 16)Recommendation engine
# Example:
# You studied Biology for only 30 minutes this week.
# Consider revising it tomorrow.

# Concepts:

# Data analysis
# Decision logic
# Functions
import datetime
import time 
import json
import threading
def load_users():
    try:
        with open("user.json", "r") as f:
            data = json.load(f)

        users = []

        for user_data in data:

            user = User(user_data["user_name"])
            user.total_minutes_studied = user_data["total_minutes_studied"]
            user.streak = user_data["streak"]
            user.achievements = user_data["achievements"]

            for session_data in user_data["sessions"]:

                start_time = datetime.datetime.fromisoformat(session_data["start_time"])

                end_time = datetime.datetime.fromisoformat(session_data["end_time"] )

                session = StudySession(start_time, end_time)

                user.sessions.append(session)

            users.append(user)

        return users

    except FileNotFoundError:
        return []
      
         
class User:
    def __init__(self,user_name):
        self.user_name = user_name
        self.tasks = []
        self.total_minutes_studied = 0
        self.streak = 0
        self.sessions = []
        self.achievements = []

def load_tasks(user_name):
 try:
  with open("tasks.json","r")as f :
    data = json.load(f)
    tasks = []
  for item in data:
    if item["user_name"] == user_name:
     task = Task(item["user_name"], item["title"], item["subject"], deadline=datetime.datetime.fromisoformat(item["deadline"]),target_minutes=item["target_minutes"] ,completed=item["completed"], reminded=item["reminded"], priority=item["priority"], minutes_studied=item["minutes_studied"])
     tasks.append(task)
  return tasks
   
 except FileNotFoundError:
    return []
   
class Task:
    
    def __init__(self,user_name, title, subject,deadline,completed=False,reminded = False,priority=None, minutes_studied=0,target_minutes=0):
        self.user_name = user_name
        self.title = title
        self.subject = subject
        self.completed = completed
        self.reminded = reminded
        self.priority = priority
        self.deadline = deadline
        self.minutes_studied = minutes_studied
        self.target_minutes = target_minutes
    
        
priority_order = {
    "High": 1,
    "Medium": 2,
    "Low": 3
}

def add_tasks(user):

    while True:
        title = input("Enter task: ")
        subject = input("Enter subject: ")
        while True:
         deadline = input("Enter deadline (DD-MM-YYYY HH:MM): ")

         try:
           deadline = datetime.datetime.strptime(deadline,"%d-%m-%Y %H:%M"  )
           break
         except ValueError:
            print("Invalid date. Please use DD-MM-YYYY HH:MM.")
        while True:
         priority = input("Enter priority (high/medium/low): ").strip().capitalize()
         if priority in priority_order:
             break
         print("Invalid priority.")
        new_task = Task(user.user_name, title, subject, deadline, priority=priority)

        user.tasks.append(new_task)
        choice = input("Do you want to add another task? (yes/no): ").lower()
        if choice != "yes":
           break
def sort_tasks(user):
  user.tasks.sort(key =lambda task: priority_order[task.priority])
        
  return user.tasks

class StudySession:
 def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.duration = self.calculate_duration()

 def calculate_duration(self):
        duration = self.end_time - self.start_time
        duration = duration.total_seconds() / 60  # Convert to minutes
        return duration
 
def countdown(user):
    """Starts a study session for a selected task."""

    today = None

    while True:
        task_no = input("Which task do you want to do? ")

        # User pressed Enter without choosing a task
        if task_no == "":
            print("No task completed.")
            break

        # Check that the task number is valid
        try:
            task_no = int(task_no)
        except ValueError:
            print("Invalid task number.")
            continue

        if task_no < 1 or task_no > len(user.tasks):
            print("Task number does not exist.")
            continue
        task = user.tasks[task_no-1]

        # Get study duration

        task.target_minutes  = int(input("Enter study time (minutes): "))
        remaining_seconds = task.target_minutes * 60

        # Record the start time
        start_time = datetime.datetime.now()

        # Countdown timer
        while remaining_seconds > 0:
            time.sleep(1)
            remaining_seconds -= 1

            minutes = remaining_seconds // 60
            seconds = remaining_seconds % 60

            print(f"{minutes:02}:{seconds:02}")

        print("Study session finished!")

        ask = input("Have you completed your task? (yes/no): ").lower()
        end_time = datetime.datetime.now()
        today = datetime.date.today()
        session = StudySession(start_time, end_time)
        

        if ask == "yes":
            print("\nStudy Session")
            print("=" * 20)
            print("Start:", session.start_time.strftime("%Y-%m-%d %H:%M:%S"))
            print("End:", session.end_time.strftime("%Y-%m-%d %H:%M:%S"))
            print(f"Duration: {session.duration:.2f} minutes")
            print("=" * 20)

            # Update user information
            user.sessions.append(session)

            task = user.tasks[task_no - 1]
            task.completed = True
            task.minutes_studied += session.duration

            user.total_minutes_studied+= session.duration

            print(f"Task {task_no} completed.")

        elif ask == "no":
             user.sessions.append(session)
             task = user.tasks[task_no - 1]
             task.completed = False
             task.minutes_studied += session.duration
             user.total_minutes_studied+= session.duration
        
        break

    return today

def check_reminders(user):
    current_time = datetime.datetime.now()

    for task in user.tasks:
        if not task.completed:
            time_difference = task.deadline - current_time
            hours_remaining = time_difference.total_seconds() / 3600

            if 0 < hours_remaining <= 2 and not task.reminded:
                print(f"Reminder: {task.title} is due in {hours_remaining:.2f} hours.")
                task.reminded = True

def run_reminder_thread(user):
    while True:
        check_reminders(user)
        time.sleep(60)  

  
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
       
def total_study_time(user):
   total = 0
   for task in user.tasks:
      total += task.minutes_studied
   return total
         
def display_tasks(user):     
    print("\nYour Tasks\n")
    for i, task in enumerate(user.tasks, start=1):
            print(f"Task {i}")
            print(f"Task Name : {task.title}")
            print(f"Subject   : {task.subject}")
            print(f"Deadline :{task.deadline}")
            print(f"Priority  : {task.priority}")
            status = "Completed" if task.completed  else "Pending"
            print(f"Status     : {status}")
            reminder = "Reminder set" if task.reminded else "No reminder"
            print(f"Reminder  : {reminder}")
            print(f"Minutes_Studied : {task.minutes_studied:.2f}")
            print("-" * 25)

def save_tasks(user):
   with open("tasks.json","r")as f :
     data = json.load(f)

   data = [item for item in data if item["user_name"] != user.user_name]

   for task in user.tasks:
      dictionary = {
         "user_name": user.user_name,
         "title": task.title,
         "subject": task.subject,
         "deadline":task.deadline.isoformat(),
         "priority": task.priority,
         "completed": task.completed,
         "reminded": task.reminded,
         "target_minutes":task.target_minutes,
         "minutes_studied": task.minutes_studied,
    
       }

      data.append(dictionary)
      with open("tasks.json", "w") as f:
        json.dump(data,f)

def count_completed(user):    
 count = 0       
 for task in user.tasks:  
     if task.completed :  
      count += 1
 return count

def calculate_percentage(completed_tasks,total_tasks):
  percentage =(completed_tasks/total_tasks)*100
  return percentage

def study_statistics(user):
 study_stats={}
 for task in user.tasks:
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

def leaderboard(users):
   sorted_users = sorted(users, key=lambda user: user.total_minutes_studied, reverse=True)
   print("\nLeaderboard\n")
   for rank, user in enumerate(sorted_users, start=1):
      print(f"{rank}. {user.user_name} - {user.total_minutes_studied:.2f} minutes")


def check_achievements(user):
    for task in user.tasks:
        if task.completed and "First task completed" not in user.achievements:
            user.achievements.append("First task completed")
            print(f"Achievement unlocked: First task completed for {task.title}!")

    if user.total_minutes_studied >= 600 and "Studied for 10 hours" not in user.achievements:
        user.achievements.append("Studied for 10 hours")
        print("Achievement unlocked: Studied for 10 hours!")

    if user.streak >= 7 and "7-day streak" not in user.achievements:
        user.achievements.append("7-day streak")
        print("Achievement unlocked: 7-day streak!")

def save_users(users):
    data = []

    for user in users:

        sessions_data = []

        for session in user.sessions:
            session_dict = {
                "start_time": session.start_time.isoformat(),
                "end_time": session.end_time.isoformat(),
                "duration": session.duration
            }

            sessions_data.append(session_dict)

        dictionary = {
            "user_name": user.user_name,
            "total_minutes_studied": user.total_minutes_studied,
            "streak": user.streak,
            "achievements": user.achievements,
            "sessions": sessions_data
        }

        data.append(dictionary)

    with open("user.json", "w") as f:
        json.dump(data, f)

def recommendation_engine(user):
   for task in user.tasks:
     remaining = task.target_minutes - task.minutes_studied
     if remaining > 0 :
       print(f"{task.subject} needs attention")

def main():
    users= []
    users = load_users()
    for user in users:
        user.tasks = load_tasks(user.user_name)
    # Create the current user
    user_name = input("Enter your name: ")
    if user_name in [user.user_name for user in users]:
        user = next(user for user in users if user.user_name == user_name)
    else:
        user = User(user_name)
        users.append(user)
    user.tasks = load_tasks(user.user_name)

    add_tasks(user)
    sort_tasks(user)
    thread = threading.Thread(target=run_reminder_thread, args=(user,))
    thread.daemon = True  # Daemonize thread to exit when main program exits
    thread.start()

    # Start a study session
    today = countdown(user)
  
    # Update streak if the user studied today
    if today is not None:
        save_study_date(today)

        user.streak = display_streak(today)

        if user.streak == 1:
            print(f"Current streak: {user.streak} day")
        else:
            print(f"Current streak: {user.streak} days")

    check_achievements(user)

    # Calculate total study time
    user.total_minutes_studied = total_study_time(user)

    hours = user.total_minutes_studied // 60
    minutes = user.total_minutes_studied % 60

    hour_word = "hour" if hours == 1 else "hours"
    minute_word = "minute" if minutes == 1 else "minutes"

    print(f"You studied for {hours:.0f} {hour_word} {minutes:.2f} {minute_word}")

    # Display and save tasks
    display_tasks(user)
    save_tasks(user)

    # Progress statistics
    completed_tasks = count_completed(user)

    try:
        percentage = calculate_percentage(completed_tasks, len(user.tasks))
    except ZeroDivisionError:
        percentage = 0.0

    print(f"{percentage:.2f}% completed")
    print(f"{completed_tasks} out of {len(user.tasks)} tasks completed")

    # Subject statistics
    study_stats = study_statistics(user)

    for subject in study_stats:
        total_minutes = study_stats[subject]
        hours = total_minutes // 60
        minutes = total_minutes % 60

        print(f"{subject}: {hours:.0f} hours {minutes:.0f} minutes")

    highest_minutes, best_subject = most_studied_subject(study_stats)

    best_hours = highest_minutes // 60
    best_minutes = highest_minutes % 60

    print(
        f"Most studied subject: "
        f"{best_subject} ({best_hours:.0f} hours {best_minutes:.0f} minutes)"
    )
    leaderboard(users)
    save_users(users)
    recommendation_engine(user)
main()
