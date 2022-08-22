import random
print('Olá, amiguinho(a)')
print('Vamos jogar um joguinho?')
lista = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0, 2)
ps = int(input('''Faça Sua Jogada:
0 = Pedra
1 = Papel
2 = Tesoura'''))
print('**--**' *20)
print('O computador jogou {}'.format(lista[pc]))
print('O Usuario jogou {}'.format(lista[ps]))
print('**--**' *20)
if pc == ps:
    print('Empate')
elif pc == 0 and ps == 1 or pc == 1 and ps == 2 or pc == 2 and ps == 0:
    print('O Jogador ganhou')
elif pc == 1 and ps == 0 or pc == 2 and ps == 1 or pc == 0 and ps == 2:
    print('O computador ganhou')
else:
    print('Opção Invalida')


