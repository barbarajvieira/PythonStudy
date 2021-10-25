#crie um programa que leia o nome da pessoa e diga se ela tem Silva no nome
nome = input('Digite o seu nome: ').strip()
nometitle = nome.title()
teste = 'Silva' in nometitle
print('Veja se voce tem Silva no nome: {}.'.format(teste))