salário = float(input('Qual é o salário do funcionário: '))
if salário <= 1250:
    novo = salário + (salário * 0.15)
else:
    novo = salário + (salário * 0.10)
print('Quem ganhava \033[7;40m{:.2f}\033[m passa a ganhar \033[1;4;7;40m{:.2f}\033[m'.format(salário, novo))