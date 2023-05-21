import math

a = float(input("Digite aqui o valor de a: "))
b = float(input("Digite aqui o valor de b: "))
c = float(input("Digite aqui o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    bhaskara1 = (-b + math.sqrt(delta)) / (2 * a)
    print("a raiz desta equação é:", bhaskara1)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        bhaskara1 = (-b + math.sqrt(delta)) / (2 * a)
        bhaskara2 = (-b - math.sqrt(delta)) / (2 * a)

    elif bhaskara1 > bhaskara2:
    print("as raízes da equação são", bhaskara1, "e", bhaskara2)
    else:
    print("as raízes da equação são", bhaskara2, "e", bhaskara1)
