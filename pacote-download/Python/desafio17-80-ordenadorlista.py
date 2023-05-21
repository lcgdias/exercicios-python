lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #lista-1 se refere ao ultimo elemento da lista
        lista.append(n)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista): #vai de 0 até a ultima posicao
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posicao {pos}...')
                break
            pos += 1
print(f'Os valores digitados foram: {lista}')