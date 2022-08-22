
n1 = float(input('Digite o 1° numero'))
n2 = float(input('Digite o 2° numero'))
n3 = float(input('Digite o 3° numero'))
if n1 > n2 and n1 > n3:
    print('o Maior numero é {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('o Maior numero é {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('o Maior numero é {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('o Menor numero é {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('o Menor numero é {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('o Menor numero é {}'.format(n3))
