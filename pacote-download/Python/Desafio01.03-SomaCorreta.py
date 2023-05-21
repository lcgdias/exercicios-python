n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
s = n1 + n2
print('\033[31m=*\033[m'*20)
print('A soma de \033[31m{}\033[m + \033[31m{}\033[m vale \033[4;36m{}\033[m'.format(n1, n2, s))