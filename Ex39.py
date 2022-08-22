ano = int(input('Digite o ano do seu nascimento'))
idade = 2022 - ano
if idade > 18:
    print('Já passou o tempo de se alistar')
    p = idade - 18
    print('Já se passaram {} anos que você deveria ter se alistado'.format(p))
elif idade == 18:
    print('Está no momento de se alistar')
else:
    print('Você ainda vai precisar se alistar')
    p = 18 - idade
    print('Ainda faltam {} anos para você se alistar'.format(p))

