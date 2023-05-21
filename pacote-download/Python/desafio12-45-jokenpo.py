from random import choice
ppt = ['Pedra', 'Papel', 'Tesoura']
comput = choice(ppt)
usuario = str(input('Pedra, papel ou tesoura? -> ')).capitalize()
print('A maquina escolheu...')
print('=*'*20)
print(comput)
print('=*'*20)
if comput == 'Tesoura' and usuario == 'Pedra':
    print('Voce venceu!')
elif comput == 'Tesoura' and usuario == 'Papel':
    print('Voce perdeu :(')
elif comput == 'Papel' and usuario == 'Pedra':
    print('Voce venceu!')
elif comput == 'Papel' and usuario == 'Tesoura':
    print('Voce perdeu :(')
elif comput == 'Pedra' and usuario == 'Papel':
    print('Voce venceu!')
elif comput == 'Pedra' and usuario == 'Tesoura':
    print('Voce perdeu :(')
elif comput == usuario:
    print('Deu empate...')