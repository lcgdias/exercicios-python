a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))
if a < b + c and b < a + c and c < a + b:
    triangulo = True
    print('Eh um triangulo!')
else:
    print('Nao eh um triangulo...')
if triangulo == True and a == b == c:
    print('E ele eh equilatero :)')
elif triangulo == True and a == b or a == c or b == c:
    print('E ele eh isosceles :)')
elif triangulo == True and a != b != c:
    print('E ele eh escaleno :)')