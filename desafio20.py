#Professor quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada
import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
ordem = random.sample(lista, 4)
print('A ordem de apresentação é: {}'.format(ordem))