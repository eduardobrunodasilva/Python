"""Crie um programa que leia o nome da pessoa
e diga se tem o "SILVA" no nome"""

nome = str(input('Qual é o seu nome? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))