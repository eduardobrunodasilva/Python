n1 = int(input('Um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2
print('A soma é {}, o produto é {}, a divisão é {:.2f}'.format(s, m, d))
print('A divisão inteira é {}, potência é {} e o resto é {}'.format(di, e, r))
