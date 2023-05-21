cont = True
qntd = 0
soma = 0
maior = 0
menor = 0
while cont:
    n = int(input('Digite um numero inteiro: '))
    qntd += 1
    soma += n
    if qntd == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont = str(input('Voce deseja continuar? [S/N] '))
    if cont == 'S':
        cont = True
    else:
        cont = False
        media = soma / qntd
        print('A media dos valores digitados eh igual a {}'.format(media))
        print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))