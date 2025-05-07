"""n = int(input('Digite um número: '))
for c in range (0,n):
    print(c)
print('fim')"""

"""i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('Fim')"""

s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print('a soma de todos os valores foi {}'. format(s))