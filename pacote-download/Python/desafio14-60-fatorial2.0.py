f = int(input('Fatorial de: '))
c = f
fatorial = 1
while c > 0:
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    fatorial *= c
    c -= 1
print(fatorial)