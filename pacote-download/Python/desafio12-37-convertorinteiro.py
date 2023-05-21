n = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINARIO \n[ 2 ] converter para OCTAL \n[ 3 ] converter para HEXADECIMAL')
resp = int(input('Sua opção: '))
if resp == 1:
    print('O numero {} convertido para binario é igual a {}'.format(n, bin(n) [2:]))
elif resp == 2:
    print('O numero {} convertido para octal é igual a {}'.format(n, oct(n) [2:]))
elif resp == 3:
    print('O numero {} convertido para hexadecimal é igual a {}'.format(n, hex(n) [2:]))