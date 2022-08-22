r1 = float(input('Informe o tamanho da primeira reta'))
r2 = float(input('Informe o tamanho da segunda reta'))
r3 = float(input('Informe o tamanho da terceira reta'))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Essas retas podem formar um triangulo')
else:
    print('Essas tres retas não podem formar um triangulo')
