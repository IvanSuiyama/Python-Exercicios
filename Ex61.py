print('Gerador de PA')
print('=-'*10)
primeiro = int(input('Digite o primeiro termo'))
razao = int(input('Digite a razão'))
i = 1
termo = primeiro
while i <= 10:
    print('{} --> '.format(termo), end='')
    termo += razao
    i += 1
print('Fim')