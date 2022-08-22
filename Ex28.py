import random
na = random.randint(1, 5)
print('O computador vai escolher um numero inteiro entre 1 e 5, você consegue adivinhar qual é?')
nu = int(input('Digite o numero que o computador escolheu'))
if na == nu:
    print('Parabéns, você adivinhou')
else:
    print('Não foi dessa vez, o numero escolhido foi {}, mais sorte na proxima'.format(na))
