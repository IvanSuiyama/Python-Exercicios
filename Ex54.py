m = 0
s = 0
for i in range(0, 7):
    ano = int(input('Digite o ano de seu nascimento'))
    if 2022 - ano >= 21:
        s = s + 1
    else:
        m = m + 1
print('A quantidade de pessoas maiores de idade é de {} '.format(s))
print('A quantidade de pessoas menores de idade é de {} '.format(m))

