nome = str(input('Qual é o seu nome? '))
if nome == 'Eduardo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Lucas':
    print('Seu nome é bem normal no Brasil.')
elif nome in 'Ana, Cláudi, Jéssica, Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))