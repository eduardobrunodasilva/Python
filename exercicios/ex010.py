from math import hypot
#ou importar a biblioteca inteira
catA = int(input('Comprimento do cateto oposto: '))
catB = int(input('Comprimento do cateto adjacente: '))
#hipotenusa = math.sqrt((catA**2) + (catB**2))
#hipotenusa = math.sqrt(pow(catA,2) + pow(catB,2))
hipotenusa = hypot(catA,catB)
print('O valor da hipotenusa é igual a {}'.format(hipotenusa))
