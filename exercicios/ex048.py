from random import choice
from time import sleep

trincas_comuns = [
    {12, 24, 36},
    {7, 15, 49},
    {1, 13, 99}
]

quadras_comuns = [
    {12, 24, 36, 48},
    {3, 27, 63, 81},
    {0, 10, 20, 30}
]

mais_sorteados = list(range(0, 60))   # Top 60
menos_sorteados = list(range(60, 100))  # Bottom 40

def contem_trinca_ou_quadra_comum(jogo):
    jogo_set = set(jogo)
    for trinca in trincas_comuns:
        if trinca.issubset(jogo_set):
            return True
    for quadra in quadras_comuns:
        if quadra.issubset(jogo_set):
            return True
    return False

def jogo_repetido(jogo, jogos_anteriores):
    jogo_set = set(jogo)
    for j in jogos_anteriores:
        if set(j) == jogo_set:
            return True
    return False

def gerar_jogo_unico(jogos_anteriores):
    tentativas = 0
    while True:
        tentativas += 1

        jogo = set()
        pares = set()
        impares = set()

        combinacoes = [(25, 25), (30, 20)]
        num_pares, num_impares = choice(combinacoes)

        universo = mais_sorteados + menos_sorteados

        while len(pares) < num_pares:
            n = choice(universo)
            if n % 2 == 0 and n not in pares and n not in impares:
                pares.add(n)

        while len(impares) < num_impares:
            n = choice(universo)
            if n % 2 != 0 and n not in pares and n not in impares:
                impares.add(n)

        jogo = list(pares.union(impares))
        jogo.sort()

        if not contem_trinca_ou_quadra_comum(jogo) and not jogo_repetido(jogo, jogos_anteriores):
            return jogo

        if tentativas > 1000:
            raise Exception("Erro ao gerar jogo exclusivo.")

print('-' * 40)
print('         JOGA NA LOTOMANIA         ')
print('-' * 40)
quant = int(input('Quantos jogos você quer que eu sorteie? '))

jogos = []
for _ in range(quant):
    novo_jogo = gerar_jogo_unico(jogos)
    jogos.append(novo_jogo)

print('-' * 5, f'SORTEANDO {quant} JOGOS', '-' * 5)
for i, jogo in enumerate(jogos, start=1):
    print(f'Jogo {i}: {jogo}')
    sleep(1)
print('-' * 10, '< BOA SORTE! >', '-' * 10)