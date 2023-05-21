a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
# Verificando quem é o maior:
menor = a
if b < a:
    menor = b
if c < a:
    menor = c
# Verificando quem é o menor:
maior = a
if b > a:
    maior = b
if c > a:
    maior: c
# Imprimindo os resultados:
print('O maior numero digitado foi {}'.format(maior))
print('O menor numero digitado foi {}'.format(menor))