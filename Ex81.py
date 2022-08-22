numeros = list()
while True:
    numeros.append(int(input('Digite um numero inteiro')))
    op = str(input('Quer Continuar (S/N)')).upper()
    if op in 'N':
        break
print(f'A quantidade de numeros digitados foi {len(numeros)}')
numeros.sort(reverse=True)
print(f'Os numeros em ordem decrescente {numeros}')
if 5 in numeros:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado')
