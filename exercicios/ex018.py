'''
Refaça o desafio 009, mostrando a tabuada de um número que
o usuário escolher, porém utilizando um laço for
'''
num = int(input('Digite um número para ver sua tabuada: '))
for n in range (1,11):
    print('{} x {:2} = {}'.format(num, n, num * n))