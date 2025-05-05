'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a
tabela abaixo:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- de 25 a 30: sobrepeso
- de 30 a 40: obesidade
- acima de 40: obesidade morbida
'''

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
IMC = peso / (altura **2)
print('Seu imc é {:.2f}'.format(IMC))
if IMC < 18.5:
    print('ABAIXO DO PESO')
elif IMC < 24.9:
    print('Parabéns você está na faixa de PESO IDEAL')
elif IMC < 29.9:
    print('SOBREPESO')
elif IMC < 39.9:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA, cuidado!')
