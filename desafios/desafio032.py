'''
A confederação nacional de natação, precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade
- até 9 anos: mirim
- até 14 anos: infantil
- até 17 anos: junior
- até 25 anos: sênior
acima: master
'''

from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('O atleta tem {} anos'. format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 18:
    print('Classificação: Junior')
elif idade <= 25:
    print('Classificação: Senior')
else:
    print('Classificação: Master')