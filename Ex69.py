pm = man = mwomen = resp = 0
while True:
    print('-=-'*30)
    print('Cadastrando Pessoas')
    print('-=-' * 30)
    idade = int(input('Digite a Idade'))
    sexo = str(input('Digite o Sexo [M/F]'))
    if sexo in 'Mm' or sexo in 'Ff':
        if idade > 18:
            pm += 1
        if sexo in 'Mm':
            man += 1
        if sexo in 'Ff' and idade < 20:
            mwomen += 1
    else:
        sexo = str(input('Digite o Sexo [M/F]'))
    resp = str(input('Quer continuar? S/N')).upper()
    if resp == 'N':
            break
    if resp != 'S' and resp != 'N':
        resp = str(input('Quer continuar? S/N'))
print(f'{pm} Tem maior de 18 anos')
print(f'{man} Homens foram cadastrados')
print(f'{mwomen} Mulheres menores de 20 anos foram cadastradas')



