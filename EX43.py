peso = float(input('Digite Seu peso'))
altura = float(input('Digite sua Altura'))

imc = peso / altura ** 2

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 <= imc < 30:
    print('Sobre peso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Morbida')