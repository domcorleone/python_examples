"""
    Author: Eder Machado
    Description: Read data from a file in python
    Create Date: 19.10.2022 12:12 PM
"""

readFile = open("sons.txt", "r").read()
print(readFile)

# split the info

readFile = open("sons.txt", "r").read()
splitMe = readFile.split('\n')
print(splitMe)
#print(len(splitMe))

# read the file line by line (will put '\n' if there is any )

readFile = open("sons.txt", "r").readlines()
print(readFile)

