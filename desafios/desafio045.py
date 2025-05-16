'''Crie um programa que leia vários números inteiros pelo
teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou
não continuar a digitar os valores'''

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))

