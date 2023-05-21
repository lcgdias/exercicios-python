import random
x = random.randint(0, 10)
s = vitorias = 0
poui = ''
while True:
    print('=-'*15)
    print('VAMOS JOGAR PAR OU IMPAR!')
    print('=-'*15)
    n = int(input('Diga um valor: '))
    piu = str(input('Par ou Impar? [P/I] ')).upper()
    s = n + x
    if s % 2 == 0:
        poui = 'PAR'
    else:
        poui = 'IMPAR'
    print('-'*15)
    print(f'Voce jogou {n} e o computador {x}. Total de {s}. DEU {poui}')
    print('-'*15)
    if poui == 'PAR' and piu == 'P' or poui == 'IMPAR' and piu == 'I':
        print('Voce VENCEU!')
        print('Vamos jogar novamente...')
        vitorias += 1
    else:
        print('Voce PERDEU!')
        print('=-'*15)
        print(f'GAME OVER! Voce venceu {vitorias} vez(es).')
        break
