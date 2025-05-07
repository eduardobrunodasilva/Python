'''
Crie um programa que leia uma frase qualquer e diga se ela é
um palíndromo (frase lida de frente para trás e de trás
para frente que seja a mesma coisa), desconsiderando os espaços
ex.:
1. Após a sopa
2. A sacada da casa
3. A torre da derrota
4. O lobo ama o bolo
5. Anotaram a data da maratona
'''

'''frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1,-1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')'''

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')


