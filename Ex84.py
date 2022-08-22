tot = []
parcial = []
i = c = 0
maior = menor = 0
while True:
    parcial.append(str(input('Digite o nome da pessoa')))
    parcial.append(float(input('Digite o Peso')))
    if len(tot) == 0:
        maior = menor = parcial[1]
    else:
        if parcial[1] > maior:
            maior = parcial[1]
        if parcial[1] < menor:
            menor = parcial[1]
    tot.append(parcial[:])
    c += 1
    parcial.clear()
    resp = str(input('Quer Continuar? S/N'))
    if resp in 'Nn':
        break
print(f'As pessoas cadastradas foram {c}')
print(f'O maior peso foi de {maior} e os nomes com maior peso são: ', end='')
for p in tot:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {menor} e os nomes com menor peso são: ', end='')
for p in tot:
    if p[1] == menor:
        print(f'{p[0]} ', end='')


