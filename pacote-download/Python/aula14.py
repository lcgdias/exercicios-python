# Estrutura de repetição while
# while condição:
# for = utilizado quando voce sabe qual o limite do intervalo
# while = utilizado quando o limite eh desconhecido

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
print('-'*10)

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    # Para nao contabilizar o 0
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares.'.format(par, impar))