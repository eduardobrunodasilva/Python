'''Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
A) quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) quais foram os números pares'''

núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 foi digitado na {núm.index(3)+1}ª')
else:
    print('O valor 3 não foi digitado em nenhum aposição')
print('Os valores pares digitados foram: ', end='')
for n in núm:
    if n % 2 == 0:
      print(n, end=' ')