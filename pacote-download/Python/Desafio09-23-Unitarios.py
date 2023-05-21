# como string
n = str(input('Digite um numero entre 1 e 9999: '))
print(' milhar: {} \n centenas: {} \n dezenas: {} \n unidades: {}'.format(n[0], n[1], n[2], n[3]))

# como numero
n = int(input('Digite um numero entre 1 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(' milhar: {} \n centenas: {} \n dezenas: {} \n unidades: {}'.format(m, c, d, u))