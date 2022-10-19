"""
    Author: Eder Machado
    Description: Final Assignment - Grading System
    Created Date: 19.10.2022
"""
from statistics import *
# declare an dictionary of students

username = "admin"
password = "admin123"

students = {'Alex':[92, 76, 88],
            'Jeff': [78, 88, 93],
            'Sam': [89, 92, 93]}
# function

def goOut():
    print("Good bye...")
    #exit()
    
# creating the menu

def menu():
    valid = True
    while valid:
        print("\tWelcome to Grade Central\n")
        print("\t[1] - Enter Grades")
        print("\t[2] - Remove Student")
        print("\t[3] - Students Average Grades")
        print("\t[4] - Exit\n")

        op = input("What would you like to do today? (Enter a number) ")

        if op == "1":
            studentName = input("Student Name: ")
            enterGrades(studentName)
        elif op == "2":            
            studentName = input("What student to remove?: ")
            removeStudent(studentName)
        elif op == "3":            
            studentAVGs()
        elif op == "4":            
            goOut()
            valid = False
        else:
            print("Invalid option select again")

           
# enter grades

def enterGrades(std):
    found = False    
    for student in students:
        if student == std:
            found = True
    if found:
        grade = input("Grade: ")
        while not grade.isnumeric():
            print("Please insert a numeric value")
            grade = input("Grade: ")
        students[std].append(int(grade))
        print("Adding Grade...")
        print(students)
    else:
        print("Student with the name", std, "was not found")

# removing student

def removeStudent(param):
    found = False
    for student in students:
        if student == param:
            found = True
    if found:
        yes_or_no = input("are you sure you want to remove "+param+
                          "? type 'y' to remove and 'n' to cancel\n")
        if yes_or_no == 'y' or yes_or_no == 'Y':
            del students[param]
            print("removing student...")
            print(students)
        elif yes_or_no == 'n' or yes_or_no == 'N':
            print("Student with the name "+param+" will not be deleted...")
        else:
            print("You selected an invalid option to confirm the deletion...")
    else:
        print("Impossible to temove Student with the name", param)

# student AVGS

def studentAVGs():
    std = input("Enter the student to calcute the AVG: ")
    studentFound = False
    for student in students:
        if student == std:
            studentFound = True
    if not studentFound:
        print("Student with the name "+std+" was not found.")
    else:
        print("The AVG for a student '"+std+"' is ", mean(students[std]))

def login():
    user = input("Username: ")
    pwd = input("Password: ")
    
    if username == user and password == pwd:
        print("Login was sucessful")
        menu()
    else:
        print("Invalid passoword, will detonate in 5 seconds!")
def main():
    login()
    
main()


        
