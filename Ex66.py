c = s = 0
while True:
    n = int(input('Digite um numero inteiro [999 para parar]'))
    if n == 999:
        break
    c += 1
    s += n
print(f'{c} foram digitados e a soma entre eles é de {s}')
