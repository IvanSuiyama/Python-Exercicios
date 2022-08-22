valores = list()
while True:
    n = int(input('Digite um valor inteiro'))
    if n not in valores:
        valores.append(n)
    else:
        print('Esse valor ja existe')
    op = str(input('Quer continuar? S/N'))
    if op in 'Nn':
        break
valores.sort()
print(f'Os valores digitados foram {valores}')

