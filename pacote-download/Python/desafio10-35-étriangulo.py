a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))
# Verificando os lados
if a < b + c and b < a + c and c < a + b:
    print('Eh um triangulo!')
else:
    print('Nao eh um triangulo!')


