n = int(input('Digite um numero inteiro'))
print(' A TABUADA do Numero {} é '.format(n))
for i in range(1, 11):
    M = n * i
    print('{} x {} = {}'.format(n, i, M))
    i += i
print('FIM')
