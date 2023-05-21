n = int(input('Numero inteiro: '))
nd = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[031m', end='')
        nd += 1
    else:
        print('\033[037m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi dividido um total de {} vezes'.format(n, nd))
if nd == 2:
    print('Logo, esse numero EH primo.')
else:
    print('Logo, esse numero EH primo.')