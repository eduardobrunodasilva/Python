from random import randint, choice, sample
from time import sleep
from itertools import combinations


trincas_comuns = [
    {5, 10, 23},
    {27, 30, 42},
    {8, 23, 33}
]

quadras_comuns = [
    {5, 10, 23, 33},
    {8, 27, 30, 42},
    {10, 23, 30, 53}
]


mais_sorteados = [5, 10, 23, 33, 42, 53, 27, 8, 30, 47]
menos_sorteados = [3, 14, 21, 36, 44, 60, 2, 18, 39, 49]

# Blocos de dezenas
blocos = {
    1: list(range(1, 16)),
    2: list(range(16, 31)),
    3: list(range(31, 46)),
    4: list(range(46, 61))
}

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
    for j in jogos_anteriores:
        if set(j) == set(jogo):
            return True
    return False

def gerar_jogo_unico(jogos_anteriores):
    tentativas = 0
    while True:
        tentativas += 1
        pares = set()
        impares = set()
        combinacoes = [(3, 3), (4, 2), (2, 4)]
        num_pares, num_impares = choice(combinacoes)

        # Um número de cada bloco
        numeros_possiveis = [choice(bloco) for bloco in blocos.values()]


        while len(numeros_possiveis) < 6:
            candidato = choice(mais_sorteados if randint(0, 1) else menos_sorteados)
            if candidato not in numeros_possiveis:
                numeros_possiveis.append(candidato)


        for num in numeros_possiveis:
            if num % 2 == 0 and len(pares) < num_pares:
                pares.add(num)
            elif num % 2 != 0 and len(impares) < num_impares:
                impares.add(num)

        while len(pares) < num_pares:
            num = randint(1, 60)
            if num % 2 == 0 and num not in pares and num not in impares:
                pares.add(num)
        while len(impares) < num_impares:
            num = randint(1, 60)
            if num % 2 != 0 and num not in pares and num not in impares:
                impares.add(num)

        jogo = list(pares.union(impares))
        jogo.sort()

        if not contem_trinca_ou_quadra_comum(jogo) and not jogo_repetido(jogo, jogos_anteriores):
            return jogo

        if tentativas > 1000:
            raise Exception("Muitas tentativas sem conseguir gerar jogo único e válido.")

print('-' * 30)
print('       JOGA NA MEGA SENA       ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))

jogos = []
for _ in range(quant):
    novo_jogo = gerar_jogo_unico(jogos)
    jogos.append(novo_jogo)

print('-' * 3, f'SORTEANDO {quant} JOGOS', '-' * 3)
for i, jogo in enumerate(jogos, start=1):
    print(f'Jogo {i}: {jogo}')
    sleep(1)
print('-' * 5, '< BOA SORTE! >', '-' * 5)