salário = float(input('Qual é o salário do funcionário: '))
if salário <= 1250:
    novo = salário + (salário * 0.15)
else:
    novo = salário + (salário * 0.10)
print('Quem ganhava {:.2f} passa a ganhar {:.2f}'.format(salário, novo))