s = float(input('Digite seu salario'))
if s > 1250.00:
    print('Seu novo salario com um aumento de 10% é de R${:.2f}'.format(s + (s * 0.10)))
else:
    print('Seu novo salario com um aumento de 15% é de R${:.2f}'.format(s + (s * 0.15)))
