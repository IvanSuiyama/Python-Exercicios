vc = float(input('Qual o valor da casa que você deseja comprar ?'))
s = float(input('Qual o valor do seu salario ?'))
ano = int(input('Em quantos anos você pretende pagar as presteções ?'))
vda = vc / ano
vpm = vda / 12
sp = s * (0.30)
if vpm > sp:
    print('Lamento, mas o seu emprestimo foi negado')
else:
    print('Seu emprestimo foi aprovado')
