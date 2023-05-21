from random import randint
lista = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:')
for n in lista:
    print(f'{n} ', end='')
# Eu pensei nessa solucao aqui:
organizado = (sorted(lista))
print(f'\nO menor numero da lista foi {organizado[0]}')
print(f'O maior numero da lista foi {organizado[4]}')

# Solucao mais simples do CEV:
print(f'\nO menor numero da lista foi {min(lista)}')
print(f'O maior numero da lista foi {max(lista)}')