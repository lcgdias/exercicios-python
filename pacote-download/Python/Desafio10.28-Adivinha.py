import random
x = random.randint(0, 5)
resp = int(input('Tente adivinhar qual número entre 0 a 5 a máquina vai pensar: '))
print('... PENSANDO ...')
if resp == x:
    print('É exatamente esse número!')
else:
    print('Puts! Errou... O número era {}.'.format(x))