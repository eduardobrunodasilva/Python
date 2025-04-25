real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.68
print('Com R${:.2f} você consegue comprar US${:.2f}'. format(real, dolar))