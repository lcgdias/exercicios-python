altura = float(input('Sua altura (m): '))
peso = float(input('Seu peso (kg): '))
imc = peso / altura**2
if imc <= 18.5:
    print('Voce esta abaixo do peso ideal.')
elif imc > 18.5 and imc <= 25:
    print('Voce esta no seu peso ideal.')
elif imc > 25 and imc <= 30:
    print('Voce esta com sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Voce esta com obesidade.')
elif imc > 40:
    print('Voce esta com obesidade morbida.')