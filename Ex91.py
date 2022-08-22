from random import randint
dados = {'Jogador1':randint(1, 7), 'Jogador2':randint(1, 7), 'Jogador3':randint(1, 7), 'Jogador4':randint(1, 7)}
for k, v in dados.items():
    print(f' O {k} tirou {v} no dado')



