vn = float(input('Digite o Valor normal do produto'))
print('Escolha uma opção de pagamento')
op = int(input(('1 - A Vista \n 2- A Vista no Cartão \n 3- Em ate 2x no Cartão \n 4- Em 3x ou mais no Cartão')))
if op == 1:
    print('O Preço do produto com desconto de 10% é de {}'.format(vn - (vn * (0.10))))
elif op == 2:
    print('O preço do produto com 5% de desconto é de {}'.format(vn - (vn * (0.05))))
elif op == 3:
    print('O preço do produto é de {}'.format(vn))
elif op == 4:
    print('O preço do produto com 20% de Juros é de {}'.format (vn + (vn * (0.20))))
else:
    print('Opção invalida')
