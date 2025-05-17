'''crie um programa que leia o nome e o preço de vários
produtos. o programa deverá perguntar se o usuário vai continuar.
No final, mostre:
- qual é o total gasto na compra.
- quantos produtos custam mais de R$1000
- qual é o nome do produto barato'''
print('_'*30)
print('{:^30}'.format('LOJA DO DUDU'))
print('_'*30)
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' Fim do programa '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de 1000 reais')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')