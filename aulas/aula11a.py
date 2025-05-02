""" Colocando cores em Python
[Style; Letra; Back
\033[0;30;41m > Letra branca, fundo vermelho
\033[4;33;44m > sublinhado, letra amarela, fundo azul
\033[1;35;43m > negrito, texto amarelo e fundo azul
\033[30;42m > letra branca, fundo verde
\033[m > Padrão - letra cinza fundo preto
\033[7;30m > letra preta, fundo branco (inversão) """

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!'.format(a, b))

