preco = float(input('Digite aqui o valor do produto: R$'))
desconto = (preco*5)/100
print('Na liquidação de 5% de desconto, esse produto estará por R${:.4}'.format(preco - desconto))