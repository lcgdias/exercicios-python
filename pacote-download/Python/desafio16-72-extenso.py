extenso = ('zero' 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesseter', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if n < 0 and n > 20:
        break
    print('Tente novamente. ', end='')
print(f'Voce digitou o numero {extenso[n - 1]}')