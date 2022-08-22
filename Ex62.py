print('Gerador de PA')
print('=-'*10)
primeiro = int(input('Digite o primeiro termo'))
razao = int(input('Digite a razão'))
i = 1
total = 0
termo = primeiro
mais = 10
while mais != 0:
    total += mais
    while i <= total:
        print('{} --> '.format(termo), end='')
        termo += razao
        i += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos '.format(total))
