n = 1
qntd = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero inteiro: '))
    # Para nao contar o flag
    if n!= 999:
        qntd += 1
        soma += n
print('Foram digitados {} valores.'.format(qntd))
print('A soma desses valores eh igual a {}.'.format(soma))