preco = float(input('Valor do produto: R$'))
print('Formas de pagamento: \n [ 1 ] A vista/cheque \n [ 2 ] A vista no cartão \n [ 3 ] 2x no cartão \n [ 4 ] 3x ou mais no cartão')
opcao = int(input('Sua opcao: '))
if opcao == 1:
    desc = (preco * 10)/100
    print('Por comprar assim, o valor do produto agora eh R${:.2f}'.format(preco - desc))
elif opcao == 2:
    desc = (preco * 5)/100
    print('Por comprar assim, o valor do produto agora eh R${:.2f}'.format(preco - desc))
elif opcao == 3:
    parc = preco / 2
    print('Nao ha desconto nessa forma de pagamento. O preco sao duas parcelas de R${:.2f}'.format(parc))
elif opcao == 4:
    juros = (preco * 20)/100
    print('O produto tera 20% de juros e ficara valendo R${:.2f}'.format(preco + juros))