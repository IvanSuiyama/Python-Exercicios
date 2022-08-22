num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero entre 0 e 20'))
    if 0 <= n <= 20:
        print(f'Você digitou o numero {num[n]}')
        break
    else:
        print('Tente de novo. Digite um numero entre 0 e 20')
