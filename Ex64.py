i = n = soma = 0
n = int(input('Digite um valor [999 para parar]'))
while n != 999:
    i += 1
    soma += n
    n = int(input('Digite um valor [999 para parar]'))
print('Você digitou {} valores e a soma entre eles foi {} '.format(i, soma))
print('FIM')
