frase = str(input('Digite uma frase')).strip().upper()
palavra = frase.split()
j = ''.join(palavra)
inverso = ''
for letra in range (len(j) -1, -1, -1):
    inverso += j[letra]
if inverso == j:
    print('Essa frase {} é uma palindroma'.format(frase))
else:
    print('')

