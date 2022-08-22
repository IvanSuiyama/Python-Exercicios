from random import randint
n = ((randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)))
print(f'Os valores Sorteados Foram: ', end='')
print(f'{n}', end='')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')

