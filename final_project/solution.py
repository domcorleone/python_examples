"""
    Author: Eder Machado
    Description: Implemeting the solution given by the trainer
    Created Date: 20.10.2022 02:01 PM
"""
from statistics import mean as m

admins = {'Python':'Pass123@', 'user2':'pass2'}

studentDict = {'Alex':[78,88,93],
               'Jeff':[92,76,88],
               'Sam':[89,92,93]}

def enterGrades():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exist.')
    print(studentDict)

def removeStudent():
    nameToRemove = input('What Student to remove?: ')
    
    if nameToRemove in studentDict:
        print('Removing Student...')
        del studentDict[nameToEnter]
    else:
        print('Student to remove does not exist.')
    print(studentDict)

def calculateAVGs():
    nameTocalculateAVGs = input('Enter the Student to calculate the AVGs?: ')
    
    if nameTocalculateAVGs in studentDict:
        print('Calculating the Student AVGs...')
        print( 'The AVGS of the student ',nameTocalculateAVGs, "is: ",
               m(studentDict[nameTocalculateAVGs]) )
    else:
        print('Student to calculate the AVG does not exist.')
    print(studentDict)

def studentAVGs():
    newDict = {}
    for student in studentDict:
        gradesList = studentDict[student]
        studentAVG = m(gradesList)
        newDict[student] = studentAVG
        print(student,' AVG: ', studentAVG)
    print(newDict.keys())
    
    if len(newDict) > 0:      
        print('The student with the highest AVG is ', max(newDict,key=newDict.get))
    
def main():
    print("""
    Welcome to Central Grade System

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    """)

    action = input('What would you like to do today? (Enter a number) ')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAVGs()
    elif action == '4':
        exit()
    else:
        print('No valid choice was given, please try again')

login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
        print('welcome, ', login)
        while True:
            main()
    else:
        print('Invalid password, will detonate in 5 seconds!')
else:
    print('Invalid username, calling the FBI to report this ')
    


