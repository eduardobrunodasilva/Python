vel = float(input('Qual é a velocidade atual do carro? '))
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/k')
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de {:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija sempre com segurança!')