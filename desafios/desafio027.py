'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o valor da
casa, o salário do comprador e em quanto anos ele vai pagar.

Calcule o valor da prestação mensal. Sabendo que ela não pode
exceder a 30% do salário ou então o empréstimo será negado
'''

casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos de financiamento? '))
prestação = casa / (tempo * 12)
mínimo = salário * (30/100)
print('Para pagar uma casa de R$ {:.2f} em {} anos,'.format(casa, tempo), end='')
print(' a prestação será de R$ {:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')
