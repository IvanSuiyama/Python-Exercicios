tot = [[], []]
n = 0
for i in range(0, 7):
    n = (int(input('Digite um valor inteiro')))
    if n % 2 == 0:
        tot[0].append(n)
    else:
        tot[1].append(n)
tot[0].sort()
tot[1].sort()
print(f'Os valores pares são {tot[0]}')
print(f'Os valores impares são {tot[1]}')

