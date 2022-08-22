import math
co = float(input('Digite o comprimento do cateto oposto do triangulo retangulo'))
ca = float(input('Digite o comprimento do cateto adjacente do triangulo retangulo'))
hip = math.sqrt((co ** 2) + (ca ** 2))
print('O comprimento da hipotenusa do triangulo retangulo é {:.3f}'.format(hip))
