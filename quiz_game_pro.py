# Challenge 8 — Quiz Game Pro

# Program stores questions.

# Features:
# • Random question order
# • Final score
# • Percentage
# • Save highest score

# Concepts:
# • Dictionaries
# • Lists
# • Functions
# • File Handling

import json
import random

def display_welcome_message():
 try:
  with open("highest_score.json", "r") as f:
    data = json.load(f)
    previous_highest_score = data.get("highest_score", 0)
    print(f"Previous highest score: {previous_highest_score}\n")
    print("=" * 40)
    print("Welcome to Quiz Game Pro")
    print("=" * 40)
    print("Try to answer the following 10 questions.")
    print("Your score will be calculated at the end.")
    print("Let's get started!\n")
 except FileNotFoundError:
    print("No previous highest score found. Starting fresh!")
    print("Previous highest score: 0\n")

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Islamabad", "Karachi", "Peshawar"],
        "answer": "Islamabad"
        
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is 12 X 8?",
        "options": ["84", "96", "92", "108"],
        "answer": "96"
    },
    {
        "question": "Who developed Python?",
        "options": ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["String", "Integer", "Boolean", "Float"],
        "answer": "Boolean"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
        "answer": "Pacific"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Power Unit",
            "Central Program Utility",
            "Control Processing Unit"
        ],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#"
        
    }
]

def play_quiz(questions):
 random.shuffle(questions)
 score = 0
 for number, question in enumerate(questions, start=1):
  print(f"Question {number}:")
  print("-" * 30)
  print(question["question"])

  for i, option in enumerate(question["options"], start=1):
    print(f"{i}. {option}")
  while True:
   try:
    choice = int(input("Enter your choice (1-4): "))
    if 1 <= choice <= len(question["options"]):
                break     
    print("Invalid choice. Please enter a number between 1 and 4.")
    continue
   except ValueError:
    print("Invalid input. Please enter a number.")
    continue

  chosen_answer = question["options"][choice - 1]
  if chosen_answer == question["answer"]:
    print("Correct!\n")
    score += 1
  else:
    print("Wrong!")
    print(f"Your answer: {chosen_answer}")
    print(f"Correct answer: {question['answer']}\n")
 return score

def calculate_percentage(score, total_questions):
    return (score / total_questions) * 100

def load_score():
  try:
   with open("highest_score.json","r")as f :
    data = json.load(f)
    return data.get("highest_score", 0)
  except FileNotFoundError:
    return 0
  
def save_score(score):
    with open("highest_score.json", "w") as f:
        json.dump({"highest_score": score}, f)

def main():
    display_welcome_message()
    score = play_quiz(questions)
    total_questions = len(questions)
    percentage = calculate_percentage(score, total_questions)
    print(f"\nYour final score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.2f}%")
    if percentage == 100:
     print("Perfect score!")
    elif percentage >= 80:
     print("Excellent!")
    elif percentage >= 60:
     print("Good job!")
    else:
     print("Keep practicing!")
    highest_score = load_score()
    if score > highest_score:
        save_score(score)
        print(f"New highest score: {score}")
    else:
        print(f"Highest score remains: {highest_score}")
    print("Thank you for playing the Quiz Game Pro!")
main()