'''Crie um programa que simula o funcionamento de
um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor
serão entregues.
obs.: considere que o caixa possui cédulas de R$200 R$100 R$50,
R$20, R$10, e R$5'''

print('=' * 30)
print('{:^30}'.format('BANCO EB'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 200
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd}')
        if céd == 200:
            céd = 100
        elif céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco EB. Tenha um Bom dia!')


