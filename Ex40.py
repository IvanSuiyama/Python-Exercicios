n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota'))
m = (n1 + n2) / 2
if m < 5:
    print('Reprovado')
elif 5 < m < 6.9:
    print('Recuperação')
elif m >= 7:
    print('Aprovado')
