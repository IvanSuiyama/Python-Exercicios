'''import math
n = int(input('Digite um numero qualquer'))
print('O fatorial do numero {} é {}'.format(n, (math.factorial(n))))
'''



f = 1
n = int(input('Digite um numero qualquer'))
i = n
while i > 0:
    f *= i
    i -= 1
print('O fatorial do numero escolhido é {}'.format(f))
