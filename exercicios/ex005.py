salario = float(input('Digite o salário: R$'))
novoSalario = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de desconto, passa a ganhar R$ {:.2f}'.format(salario, novoSalario))
