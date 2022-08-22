print('A soma dos numeros impares e que são multiplos de 3 entre 1 e 500 é:  ')
s = 0
for i in range(1, 501):
    if i % 2 != 0:
        if i % 3 == 0:
            s += i
print(s)
