#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o 1o e o ultimo nome separadamente
nome = str(input('Digite seu nome completo: ')).strip()
split = nome.split()
print('O seu primeiro nome é: {}.'.format(split[0]))
print('O seu último nome é: {}.'.format(nome[len(nome) - 1]))
