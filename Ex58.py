import random
i = 0
print('Olá, vou pensar em um numero inteiro de 0 a 10')
print('Você consegue adivinhar qual é?')
nc = random.randint(1, 10)
print('Ja escolhi meu numero, boa sorte')
np = int(input('Qual numero você acha que eu estou pensando? '))
while nc != np:
    print('Não é esse')
    np = int(input('Digite um outro numero que você acha que eu estou pensando'))
    i += 1
print('Parabens você acertou!!!')
print('Você precisou de {} chances para acertar'.format(i))
