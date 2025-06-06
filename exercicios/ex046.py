from random import randint, choice
from time import sleep


mais_sorteados = [1, 2, 3, 5, 9, 10, 11, 13, 15, 17, 20, 21, 22, 24, 25]


menos_sorteados = [4, 6, 7, 8, 12, 14, 16, 18, 19, 23]


todos_possiveis = list(set(mais_sorteados + menos_sorteados))

def gerar_jogo_existente(jogos_existentes):
    tentativas = 0
    while True:
        tentativas += 1
        pares = set()
        impares = set()


        combinacoes = [(8, 7), (6, 9)]
        num_pares, num_impares = choice(combinacoes)

        # Candidatos válidos
        candidatos_pares = [n for n in todos_possiveis if n % 2 == 0]
        candidatos_impares = [n for n in todos_possiveis if n % 2 != 0]


        while len(pares) < num_pares:
            num = choice(candidatos_pares)
            pares.add(num)


        while len(impares) < num_impares:
            num = choice(candidatos_impares)
            impares.add(num)

        novo_jogo = list(pares.union(impares))
        novo_jogo.sort()


        jogo_valido = True
        for jogo in jogos_existentes:
            if len(set(jogo) & set(novo_jogo)) > 7:
                jogo_valido = False
                break

        if jogo_valido:
            return novo_jogo

        # Evita laço infinito
        if tentativas > 1000:
            raise Exception("Não foi possível gerar um jogo único após muitas tentativas.")


print('-' * 30)
print('       JOGA NA LOTOFÁCIL       ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))

jogos = []
for _ in range(quant):
    novo_jogo = gerar_jogo_existente(jogos)
    jogos.append(novo_jogo)

print('-' * 3, f'SORTEANDO {quant} JOGOS', '-' * 3)
for i, jogo in enumerate(jogos, start=1):
    print(f'Jogo {i}: {jogo}')
    sleep(1)
print('-' * 5, '< BOA SORTE! >', '-' * 5)