#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. Calcule e mostre o tamanho da hipotenusa
import math
c1 = float(input('Digite o tamanho do cateto oposto: '))
c2 = float(input('Digite o tamanho do cateto adjacente: '))
print('Sendo o cateto oposto {} e o cateto adjacente {}, a hipotenusa é {:.3}.'.format(c1, c2, math.hypot(c1, c2)))