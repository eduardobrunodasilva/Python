""" Crie um programa que leia o nome completo de uma pessoa e leia:
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome
"""

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))