list = ('Cell', 1500,
        'Notebook', 3000,
        'Mouse', 75,
        'Teclado', 120,
        'Acessorios', 250)
print('-' * 40)
for pos in range(0, len(list)):
        if pos % 2 == 0:
                print(f'{list[pos]:.<30}', end='')
        else:
                print(f'R$ {list[pos]:>7.2f}')
print('-' * 40)
