op = 0
n1 = float(input('Digite o primeiro numero'))
n2 = float(input('Digite outro numero'))
while op != 5:
    op = int(input('''O que você deseja fazer com os numeros acima?
    1- Somar
    2- Multiplicar
    3- Maior
    4- Novos Numeros
    5- Sair do Programa'''))
    if op == 1:
       s = n1 + n2
       print('A soma é {}'.format(s))
    if op == 2:
        m = n1 * n2
        print('A multiplicação é {}'.format(m))
    if op == 3:
        if n1 > n2:
            print('O maior numero é o {}'.format(n1))
        else:
            print('O maior numero é o {}'.format(n2))
    if op == 4:
        n1 = float(input('Digite o primeiro valor'))
        n2 = float(input('Digite outro valor'))
print('FIM')
