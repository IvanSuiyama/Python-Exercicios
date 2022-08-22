n = int(input('Digite um numero inteiro'))
m = int(input('Escolha qual a conversão desejada: \n1- Binario \n2- Octal \n3- Hexadecimal'))
if m == 1:
    print('O numero {} em Binario é {}'.format(n, bin(n)[2:]))
elif m == 2:
    print('O numero {} em Octal é {}'.format(n, oct(n)[2:]))
elif m == 3:
    print('O numero {} em Hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção invalida, Escolha somente 1, 2 ou 3')
