# Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que o ajude, lendo o nome deles e escrevendo o nome do escolhido
import random
import time

aluno = input('Digite o nome dos alunos: ')
time.sleep(5)
aluno = str(aluno).split()
print(type(aluno))
sorteado = random.choice(aluno)
print(' O aluno sorteado para limpar o quadro é: {}.'.format(sorteado))
