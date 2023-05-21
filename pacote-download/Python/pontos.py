import math

x1 = int(input("Digite a coordenada de x: "))
y1 = int(input("Digite a coordenada de y: "))
x2 = int(input("Digite a coordenada de x: "))
y2 = int(input("Digite a coordenada de y: "))

distancia = math.sqrt(((x1-x2) ** 2) + ((y1 - y2) ** 2))

if distancia >= 10:
	print("longe")
else:
	print("perto")