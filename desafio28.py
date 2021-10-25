# escreva um programa que faz o pc pensar em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir o numero escolhido.
# o programa devera escrever na tela se o usuário acertou ou nao

# print('O computador está pensando num número entre 0 e 5... Você consegue adivinhá-lo?')
# num = int(input('Em que numero estou pensando? '))
# if num == 3:
#     print('Você acertou!')
# else:
#     print('Você errou!')
from random import randint
from time import sleep

computador = randint(0,5) #faz computador pensar
print('Vou pensar em um numeor entre 0 e 5. Tente adivinhar!')
jogador = int(input('Em que numero pensei? '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Você acertou! Parabéns!')
else:
    print('Ganhei! Eu pensei no numero {} e nao no {}.'.format(computador, jogador))
