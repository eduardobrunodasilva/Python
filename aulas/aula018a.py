teste = list()
teste.append('Eduardo')
teste.append(26)
galera = list()
galera.append(teste[:])
teste[0] = 'Lucas'
teste [1] = 20
galera.append(teste[:])
print(galera)