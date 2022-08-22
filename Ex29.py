km = int(input('Qual a veocidade do seu carro em km(h)'))
if km > 80:
    print('Você está acima da velocidade permitida e foi multado')
    vm = (km - 80) * 7
    print('Sua multa vai custar R${},00'.format(vm))
else:
    print('Você está dentro do limite permitido')
