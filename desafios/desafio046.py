'''Crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. no final,
mostra quantos números foram digitados e qual foi a
soma entre eles (desconsiderando o flag)'''

n = s = cont = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma dos {cont} digitados foi {s}')