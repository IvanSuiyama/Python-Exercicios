import random
n1 = str(input('Primeiro aluno'))
n2 = str(input('Segunda aluna'))
n3 = str(input('Terceira aluna'))
n4 = str(input('Quarta aluna'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será {}'.format(lista))

