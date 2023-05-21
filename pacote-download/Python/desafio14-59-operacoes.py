n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
finalizar = False
while not finalizar:
    print('*'*10)
    print('ANALISADOR')
    print('*'*10)
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos numeros')
    print('[ 5 ] sair do programa')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        print('A soma entre {} e {} eh igual a {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('A multiplicacao entre {} e {} eh igual a {}'.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        if n2 > n1:
            maior = n2
        print('O maior numero entre {} e {} eh {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Digite aqui o primeiro numero: '))
        n2 = int(input('Digite aqui o segundo numero: '))
    elif opcao == 5:
        finalizar = True