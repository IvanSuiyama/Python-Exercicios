p = int(input('Digite o primeiro termo da PA'))
r = int(input('Digite a Razão da PA'))
for i in range(1, 11):
    print(p, end='-->')
    p = p + r
print('Acabou')
