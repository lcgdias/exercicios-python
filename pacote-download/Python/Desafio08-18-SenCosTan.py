from math import radians, cos, tan, sin
ang = float(input('Digite aqui o angulo: '))
seno= sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('Com o angulo {}, temos que seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}!'.format(ang, seno, coss, tang))