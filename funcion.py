"""
    Author: Eder Machado
    Description: Creating functions in python 3.x
    Date: 17.10.2022 15:49
"""
# global variables
x = 1
y = 10

"""
exemplo = ["Erica", "Elmer", "Evandro"]

exemplo2 = ["Delcio", "Ze", "Mita", "Lenira", "Uriel", "Yelani"]


for nome in exemplo:
    print (nome)

total = len(exemplo2)
count = 1
while ( count < total ):
    print(exemplo2[count])
    count +=1
"""

def teste():
    if x > y:
        print(x, 'is greater than', y)
    else:
        print(x,'is less than',y)
        
def exemplo():
    
    print(10+1)

# 1.call all the functions one by one
#exemplo()
#teste()

# 2.instead call all the functions via method main like this:

def main():
    exemplo()
    teste()
main()
