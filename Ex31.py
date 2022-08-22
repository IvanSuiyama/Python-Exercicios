d = float(input('Quantos quilometros tem a sua viajem ?'))
if d <= 200.0:
    print('O valor da sua viajem é R${:.2f}'.format(d * 0.50))
else:
    print('O valor da sua viajem é R${:.2f}'.format((d - 200) * 0.45))


