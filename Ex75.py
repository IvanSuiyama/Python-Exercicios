numeros = ((int(input('Digite um numero inteiro'))), (int(input('Digite um numero inteiro'))), (int(input('Digite um numero inteiro'))), (int(input('Digite um numero inteiro'))))
print(f'O numero 9 apareceu {numeros.count(9)} vezes')
print(f'A posição em que o numero 3 pareceu primeiro foi {numeros.index(3)}')
print('Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print('\n', n, end='')

