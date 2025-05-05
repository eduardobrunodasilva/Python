'''
Crie um programa que leia duas notas de um aluno e calcule a
sua média, mostrando uma mensagem no final, de acordo com a
média atingida:
- média abaixo de 5.0: REPROVADO;
- média entre 5.0 e 6.9: RECUPERAÇÃO
- média 7.0 ou superior: APROVADO
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2

if média < 5:
    print('Sua média é {:.1f}, você está REPROVADO!'.format(média))
elif 7 > média >= 5:
    print('Sua média é {:.1f}, você está de RECUPERAÇÃO!'.format(média))
else:
    print('Sua média é {:.1f}, você está APROVADO!'.format(média))