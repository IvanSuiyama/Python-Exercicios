t = 1
sexo = str(input('Digite seu Sexo')).upper()
while t == 1:
    if sexo == 'M' or sexo == 'F':
        print('Obrigado')
        t += 1
    else:
       print('Opção invalida')
       sexo = str(input('Digite seu Sexo'))


