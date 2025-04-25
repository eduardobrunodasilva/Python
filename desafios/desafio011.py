altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
litro = 2
qtdLitros = area / litro
print('Sua parede tem a dimensão {}x{} e sua área é de {}m². \nPara pintar essa parede, você precisará de {}l de tinta'.format(altura, largura, area, qtdLitros))
