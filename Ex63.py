n = int(input('Digite quantos termos você quer mostrar'))
i = 2
t1 = 0
t2 = 1
print('{} -> '.format(t1), end='')
while i <= n:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    i += 1
print('FIM')
