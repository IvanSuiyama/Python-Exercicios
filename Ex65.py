resp = 'S'
qtd = media = maior = menor = soma = 0
while resp in 'Ss':
    n = int(input('Digite um numero'))
    qtd += 1
    soma += n
    if qtd == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / qtd
print('Você digitou {} numeros e a media entre eles é {}'.format(qtd, media))
print('O maior numero digitado foi {} e o menor numeor digitado foi {}'.format(maior, menor))

