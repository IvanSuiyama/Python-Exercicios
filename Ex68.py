import random
print('PAR OU IMPAR')
i = 0
while True:
    nc = random.randint(1, 10)
    nu = int(input('Digite um numero'))
    op = str(input('P/I ?'))
    s = nc + nu
    if op in 'Ii' and s % 2 == 0:
        break
    if op in 'Pp' and s % 2 != 0:
        break
    if op in 'Pp' and s % 2 == 0:
        i += 1
        print('Parabéns você venceu')
        print(f'você jogou {nu} o computador jogou {nc} o resultado foi {s} deu PAR')
    if op in 'Ii' and s % 2 != 0:
        i += 1
        print('Parabéns você venceu')
        print(f'você jogou {nu} o computador jogou {nc} o resultado foi {s} deu IMPAR')
print(f'O computador jogou {nc} você jogou {nu} o resultado foi {s}')
print('Game Over')
print(f'Você conseguiu vencer {i} vezes')
