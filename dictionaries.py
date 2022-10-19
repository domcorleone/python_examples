"""
    Author: Eder Machado
    Description: Operation with dictionaries
    Created Date: 19.10.2022 08:57 PM
"""

gradeDict = {'David': 65, 'Kelly': 89, 'Jack': 95, 'Samantha': 78 }

print(gradeDict)

# using key to acess the value

print( gradeDict['David'] )

# assigning value to the list

gradeDict['David'] = 56

print(gradeDict)

# add student to the dictionary

gradeDict['Jessy'] = 100

print(gradeDict)

# remove someone from the list

del gradeDict['David']

print(gradeDict)

gradeDict = {'David': [120, 56],
             'Kelly': [89, 78],
             'Jack': [95, 142],
             'Samantha': [89, 85] }
print(gradeDict)
print(gradeDict['Jack'])
