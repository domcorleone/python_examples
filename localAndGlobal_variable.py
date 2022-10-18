"""
    Author: Eder Machado
    desc: Definig global and local variables
    Date: 18.10.2022 07:31
"""

x = 6
# definig 'x' as global is not considered best practice
def example3():
    global x
    x+=1
    print(x)
def example():
    z = 5
    print(z)
    
# can´t do this:
# print(z)

def example2():
    z = 7
    print(z)
    print(x)

    # can´t do this, cause Global Variable can be acessed locally but
    # can´t be modified locally
    #x+=1
    #print(x)

    # solving the issue - BEST PRACTICE
    #y = x + 1
    #print(y)
    # or
    y = x + 1
    return y

# updating the global value by assigning the function out of the function
x = example2()

print(x)
    
