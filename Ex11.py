#largura,altura,area em (m),1Litro = 2m²
L = float(input('Digite a largura da parede em (m)'))
A = float(input('Digite a altura da parede em (m)'))
ar = (L * A) ** 2
print('A área em metros quadraticos é {}'.format(ar))
ll = ar / 2
print('A quantidade de litros necessaria para pintar a parede é {}'.format(ll))



