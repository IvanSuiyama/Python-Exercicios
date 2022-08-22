ficha = {}
ficha['Nome'] = str(input('Nome do Aluno(a) '))
ficha['Media'] = float(input('Informe a média do aluno(a)'))
if ficha['Media'] >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
ficha['Situação'] = situacao
for k, v in ficha.items():
    print(f'{k} = {v}')
