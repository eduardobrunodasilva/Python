'''Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores M ou F. Caso esteja errado,
peça a digitação novamente até ter um valor correto'''

sexo = str(input('Informe o seu sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper()[0]
print('sexo {} registrado com sucesso!'.format(sexo))