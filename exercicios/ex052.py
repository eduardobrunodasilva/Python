'''Crie um programa que gerencie o aproveitamento de um
jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois via ler a quantidade de gols feitos
em cada partida. No final, tudo isso será guardado em um dicionário
incluindo o total de gols feitos durante o campeonato.'''
jogador = dict()
partidas = list()
jogador['nome'] = str(input('nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
for c in range(0,tot):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-' * 30)
print(jogador)
print('-' * 30)
for k, v in jogador. items():
    print(f'o campo {k} tem o valor {v}')
print('-' * 30)
print(f'O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i} fez {v} gols.')
print(f'Foi um total de {jogador['total']} gols.')