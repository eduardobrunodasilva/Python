'''
Escreva um programa que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para a conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convetido para OCTAL é igual a {}'. format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido em HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente!')