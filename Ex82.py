listaTotal = list()
listaPar = list()
listaImpar = list()
while True:
    n = int(input('Digite um numero inteiro'))
    listaTotal.append(n)
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)
    op = str(input('Quer continuar? S/N'))
    if op in 'Nn':
        break
listaTotal.sort()
listaPar.sort()
listaImpar.sort()
print(f'A lista Geral contem os seguintes valores: {listaTotal}')
print(f'A lista dos numeros Pares contem os seguintes valores: {listaPar}')
print(f'A lista dos numeros impares contem os seguintes valores: {listaImpar}')
