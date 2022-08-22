p = 0
n = int(input('Digite um numero inteiro'))
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[34m', end='')
        p += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
if p == 2:
    print('\n \033[mEsse numero {} é um numero primo'.format(n))
else:
    print('\n \033[mEsse numero {} não é um numero primo'.format(n))

