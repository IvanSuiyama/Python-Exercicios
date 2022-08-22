nomes = ('Ivan', 'Vivi', 'Tae', 'Keke', 'Lolita')
for p in nomes:
    print(f'\nO nome {p} possue essas vogais ', end='')
    for letra in p:
        if letra in 'AEIOU' or letra in 'aeiou':
            print(f'{letra}', end=' ')

