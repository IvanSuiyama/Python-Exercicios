lista = list()
maior = menor = 0
for i in range(0, 5):
    n = int(input('Digite um valor'))
    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        p = 0
        while p < len(lista):
            if n <= lista[p]:
                lista.insert(p, n)
                break
            p += 1
print(f'Os valores Digitados em ordem foram {lista}')




