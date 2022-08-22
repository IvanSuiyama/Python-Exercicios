somai = 0
media = 0
midadeMan = 0
nomeVelho = 0
Mu20 = 0
for p in range(1, 5):
    print('pessoa numero {}'.format(p))
    nome = str(input('Digite seu nome')).strip()
    idade = int(input('Digite sua Idade'))
    sexo = str(input('Digite seu Sexo (M/F)')).upper()
    somai += idade
    if p == 1 and sexo == 'M':
        midadeMan = idade
        nomeVelho = nome
    if sexo == 'M' and midadeMan < idade:
        midadeMan = idade
        nomeVelho = nome
    if sexo == 'F' and idade < 20:
        Mu20 += 1
media = somai / 4
print('A media de idade do grupo é {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(midadeMan, nomeVelho))
print('A quatidade de mulheres com menos de 20 anos é {}'.format(Mu20))
