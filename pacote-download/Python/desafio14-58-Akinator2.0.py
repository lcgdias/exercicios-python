import random
x = random.randint(0, 10)
acertou = False
tentat = 0
while not acertou:
    print('Tente adivinhar qual número entre 0 e 10 a máquina vai pensar...')
    resp = int(input('Sua aposta: '))
    print('... PENSANDO ...')
    if resp != x:
        print('Puts! Errou...'.format(x))
        print('Tente novamente ↓')
        print('*'*20)
        tentat += 1
    if resp == x:
        print('É exatamente esse número!')
        print('Voce precisou de \033[34m{}\033[m tentativas para acertar o numero. Ufa!'.format(tentat))
        acertou = True