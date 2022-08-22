print('Cedulas disponiveis para saque 1, 10, 20, 50')
v = int(input('Qual valor você que sacar? R$'))
tot = v
va = 50
totVa = 0
while True:
    if tot >= va:
        tot -= va
        totVa += 1
    else:
        if totVa > 0:
            print(f'{totVa} notas de {va}Reais ')
        if va == 50:
            va = 20
        elif va == 20:
            va = 10
        elif va == 10:
            va = 1
        totVa = 0
        if tot == 0:
            break

