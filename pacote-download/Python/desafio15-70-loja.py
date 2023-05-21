print('-'*30)
print('LOJA SUPER BARATAO')
print('-'*30)
totalcompras = menorpreco = mais1000 = 0
nomebarato = ' '
while True:
    continuar = ' '
    prod = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    totalcompras += preco
    if totalcompras == preco:
        menorpreco = preco
    if preco < menorpreco:
        menorpreco = preco
        nomebarato = prod
    if preco > 1000:
        mais1000 += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        print('---------- FIM DO PROGRAMA -----------')
        print(f'O total da compra foi R${totalcompras}')
        print(f'Temos {mais1000} produtos custando mais de R$ 1000.00')
        print(f'O produto mais barato foi {nomebarato} que custa R${menorpreco}')
        break
