lista = []
conti = True
while conti:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Nao sera adicionado a lista.')
    conti = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if conti == 'S':
        conti = True
    elif conti == 'N':
        break
lista.sort()
print('-='*30)
print(f'Voce digitou os valores {lista}')