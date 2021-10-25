# Faça um programa que leia um ângulo qualquer e mostre o valor do seu seno, cosseno e tangente.
import math
angulo = float(input('Digite o valor de um ângulo: '))
print('O angulo {} tem seno = {:.2f}, cosseno = {:.2f} e tangente = {:.2f}.'.format(angulo, math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))
