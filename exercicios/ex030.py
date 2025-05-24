'''Crie um programa que tenha uma tupla única com nomes
de produtos e seus respectivos preços, na sequência.
No final, mostra uma listagem de preços, organizando os dados
em forma tabular'''
listagem = ('Lápis', 1.75,
            'Borracha', 1,
            'Caderno', 14.90,
            'Caneta', 2.50,
            'Estojo', 17,
            'Mochila', 119.90,
            'Livro', 32.75,
            'Corretivo', 4.60,
            'Régua', 3.50,
            'Compasso', 6.89)
print('_' * 40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('_' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('_' * 40)
