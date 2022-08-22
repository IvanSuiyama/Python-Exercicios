matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = maior = n = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l} {c}'))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            s += matriz[l][c]
    print()
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'A soma de todos os valores pares digitados foi {s}')
print(f'A soma dos numeros da 3° coluna foi {soma}')
print(f'O maior numero da 2° linha é {maior}')



