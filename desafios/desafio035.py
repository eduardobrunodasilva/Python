'''
Elabore um programa que calcule o valor a ser pago por um
produto, considerando o seu preço normal e condição de
pagamento:
- à vista dinheiro/pix: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''
print('{:=^40}'.format('LOJAS BARBOSA'))
preço = float(input('Digite o valor a ser pago: R$'))
print('''Digite a forma de pagamento:
[1] à vista dinheiro/pix
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    totaparc = int(input('Quantas parcelas? '))
    parcela = total / totaparc
    print('Sua compra será parcelada em {}x de R$ {:.2f}'.format(totaparc, parcela))
else:
    total = preço
    print('[Opção inválida de pagamento! Tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))