ano = int(input('Digite o ano de seu nascimento'))
idade = 2022 - ano
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 20:
    print('SENIOR')
elif idade > 20:
    print('MASTER')
