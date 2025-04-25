preço = float(input('Digite o preço do produto: R$'))
desc = preço - (preço * 10 / 100)
aum = desc + (desc * 15 / 100)
print('O produto no valor de R${:.2f}, sofreu desconto de 10%, ficando com valor de R${:.2f}.\n Contudo após o desconto sofrido, sofreu aumento de 15%, ficando no valor atual de R${}'.format(preço, desc, aum))
