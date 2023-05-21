a = 0
b = 1
c = 0
n = int(input('Numero de termos de Fibonacci: '))
print(a, end=' ')
print(b, end=' ')
n -= 2
while n > 0:
    c = a + b
    print(c, end=' ')
    a = b
    b = c
    n -= 1