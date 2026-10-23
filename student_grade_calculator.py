# Qs)Write a program that calculates 
# a student's result based on marks entered by the user.

def collect_marks():
 marks =[]
 total_subjects = int(input("How many subjects do you have?"))
 for i in range (0,total_subjects,1):
    std_marks=int(input(f"Enter marks of your subject{i+1}:"))
    marks.append(std_marks)
        
 return marks

def total_marks(marks):
 total = 0
 for mark in marks:
   total+=mark
 return total

def avg_marks(total_subjects,total):
    average= total/total_subjects 
    return average

def grades(average):
   if (average >=90):
    return "Grade : A+"
   elif(average >=80):
    return "Grade : A"
   elif(average >=70):
    return"Grade : B"
   elif(average >=60):
    return"Grade : C"
   else:
    return "Fail"

def main():
    marks = collect_marks()
    total=total_marks(marks)
    print(f"You got {total} out of marks")
    total_subjects = len(marks)
    average= avg_marks(total_subjects, total)
    print(f"your average marks are {average} ")
    std_grades = grades(average)
    print(std_grades)
main()       
 
 

    