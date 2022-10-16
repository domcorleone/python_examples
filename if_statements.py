# declation of variables

x = 2
y = 7
z = 10

if x > y:
    print(x, 'is greater than', y)
if x < y:
    print(x, 'is less than', y)

if x == y:
    print(x,'is the same as ',y)

if x <= y:
    print(x, 'is less or equal to', y)

if z >= x:
    print(z, 'is greater or equal to', x)

if z > y > x:
    print(z, 'is greater than', y, 'which is greater than', x)
if z > y > x <= z > y:
    print(z, 'is greater than', y, 'which is greater than',x,'which is less or equal to',z, 'which is greater than',y)
