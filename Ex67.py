while True:
    n = int(input('Você deseja ver a Tabuada de qual valor? '))
    if n < 0:
        break
    i = 1
    while i <= 10:
        r = n * i
        print(f'{n} X {i} = {r}')
        i += 1
print('Fim do programa')
