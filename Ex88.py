from random import randint
lista = list()
jogos = list()
tot = 1
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
while tot <= qtd:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Seus numeros são: {jogos}')


