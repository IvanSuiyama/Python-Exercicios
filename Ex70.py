mp = tp = mv = nmv = 0

while True:
    np = str(input('Digite o nome do produto'))
    preco = float(input('Digite o valor do produto'))
    tp += preco
    if preco > 1000:
        mp += 1
    if mv == 0:
        mv = preco
        nmv = np
    if preco < mv:
        mv = preco
        nmv = np
    resp = str(input('Quer Continuar? S/N')).upper()
    if resp != 'S' and resp != 'N':
        resp = str(input('Quer Continuar? S/N')).upper()
    if resp == 'N':
        break
print(f'O total gasto na compra foi de R${tp}')
print(f'O menor produto foi {nmv} e custa {mv}')
print(f'{mp} Custam mais que R$ 1.000,00')


