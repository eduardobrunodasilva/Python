'''
Reforça o Desafio 35 dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado:
- equilátero: todos os lados iguais;
- isósceles: dois lados iguais;
- escaleno: todos os lados diferentes;
'''

r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo', end='')
    if r1 == r2 == r3:
        print(' EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print(' ESCALENO')
    else:
        print(' ISÓSCELES')
else:
    print('Os segmentos acima não podem formar um triângulo')