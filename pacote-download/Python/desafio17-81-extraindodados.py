lista = []
elem = 0
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    conti = str(input('Quer continuar? [S/N] ')).strip().upper()
    elem += 1
    if 'S' not in conti:
        break
print(f'Foram digitados {elem} elementos...')
print(f'Os valores digitados em ordem decrescente foram: {sorted(lista, reverse=True)}')
if 5 in lista:
    pos = 0
    for c, v in enumerate(lista):
        if v == 5:
            pos = c
    print(f'O valor 5 faz parte da lista na posicao {pos}!')
else:
    print('O numero 5 nao foi encontrado na lista!')

