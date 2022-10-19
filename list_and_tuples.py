"""
    Author: Eder Machado
    Description: List and Tuples in python 3.x
    Created Date: 19.10.2022 08:19 PM
"""

def example():
    return 45,16

a,b = example()
print(a)
print(b)

# declaring a list

numbers = [6,2,3,6,8,9,4,3]

def exampleTuples():
    return numbers

print(numbers)

# append a number to the end of the list

numbers.append(12)

print(numbers)

# insert number at specific position

numbers.insert(2, 100)

print(numbers)

# remove the 1st ocorrence of the number

numbers.remove(6)

print(numbers)

# return the pos of the given number in the list

print(numbers.index(9))

# count the ocorrence of the given number

print(numbers.count(3))

# sort a list

numbers.sort()

print(numbers)

familyNames = ["Eder", "Evandro", "Erica", "Elmer", "Tia Deth", "Délcio"]

print(familyNames)

familyNames.sort()

print(familyNames)

# reverse the list

familyNames.reverse()

print(familyNames)
#example.sort()
print(example())
