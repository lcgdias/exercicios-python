valores = tuple(int(input('Digite um numero: ')) for c in range(1, 5))
print(f'Voce digitou os valores: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 foi digitado na {valores.index(3) + 1} posicao')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao')
print(f'Os valores pares digitados foram ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')