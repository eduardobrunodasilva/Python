'''Crie uma tupla preenchida com 20 primeiros colocados
da Tabela do Campeonato Brasileiro de Futebol, na ordem
da colocação. Depois mostra:
A) apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) uma lista com os times em ordem alfabética
D)em que posição na tabela está o time do Fluminense'''

times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Bragantino',
         'Ceará', 'Bahia', 'Fluminense', 'Corinthians',
         'Atlético-MG', 'Botafogo', 'São Paulo', 'Mirassol',
         'Vasco', 'Fortaleza', 'Internacional', 'Vitória',
         'Grêmio', 'Juventude', 'Santos', 'Sport')
print('-=' * 15)
print(f'Lista de times do Brasileirão {times}')
print('-=' * 15)
print(f'Os 5 primeiros colocados são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos times são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética {sorted(times)}') # sorted torna ordenado a tupla.
print('-=' * 15)
print(f'O fluminense está na {times.index('Fluminense')+1} posição')