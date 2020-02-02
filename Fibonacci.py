# This program prints the fabonacci series -

a = 0
b = 1
print(a)
print(b)

def fabo(n):
    for i in range(2,n):
        global a,b
        c = a + b
        a = b
        b = c
        print(c)

fabo(11)
