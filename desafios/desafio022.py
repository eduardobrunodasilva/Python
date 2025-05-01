dis = float(input('Qual é a distância percorrida? '))
print('Você está prestes a começar uma viagem de {}km'.format(dis))
if dis <= 200:
    preço = dis * 0.50
else:
    preço = dis * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))


