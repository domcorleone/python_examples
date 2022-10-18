'''
   Author: Eder L. Machado
   Description: Elif statement
   Date: 17.10.2020 15:36
'''

# declaration of variables
x = 13
y = 7
z = 10

if x < y:
    print(x, 'is less than', y)
elif x < z:
    print(x,'is less than', z)
elif y < z:
    print(y, 'is less than',z,'or',z,'is greater than',y)
