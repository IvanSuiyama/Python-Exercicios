import random
print('Olá amiguinho(a), vamos jogar um joguinho?')
print('O jogo se chama Jokenpo')
n1 = 'Pedra'
n2 = 'Papel'
n3 = 'Tesoura'
ps = int(input('Qual das três opções você quer ecolher? Eu prometo que não vou roubar. \n 1- Pedra \n 2- Papel \n 3- Tesoura'))
lista = [n1, n2, n3]
pc = random.choice(lista)
if pc == n1 and ps == 1:
    print('Eu escolhi {}, deu empate'.format(pc, ps))
elif pc == n1 and ps == 2:
    print('Eu escolhi {}, Parabens você ganhou!!!'.format(pc, ps))
elif pc == n1 and ps == 3:
    print('Eu escolhi {}, Eu ganhei'.format(pc, ps))
elif pc == n2 and ps == 1:
    print('Eu escolhi {}, Eu ganhei'.format(pc, ps))
elif pc == n2 and ps == 2:
    print('Eu escolhi {}, deu empate'.format(pc, ps))
elif pc == n2 and ps == 3:
    print('Eu escolhi {}, Parabens você ganhou!!!'.format(pc, ps))
elif pc == n3 and ps == 1:
    print('Eu escolhi {}, Parabens você ganhou!!!'.format(pc, ps))
elif pc == n3 and ps == 2:
    print('Eu escolhi {}, Eu ganhei'.format(pc, ps))
elif pc == n3 and ps == 3:
    print('Eu escolhi {}, deu empate'.format(pc, ps))
else:
    print('Opção do Usuario Invalida, escolha somente 1, 2 ou 3')



