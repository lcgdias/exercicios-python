maior = 0
menor = 0
for kg in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(kg)))
    if kg == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi o de {}kg'.format(maior))
print('E o menor peso foi o de {}kg'.format(menor))