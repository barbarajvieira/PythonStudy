# Crie um programa que leia um numero real e mostre a porção inteira
from math import floor
num = float(input('digite um número: '))
print('A porçao inteira do número {} é {}'.format(num, floor(num)))

#Daria p fazer sem importar, usando int(num) no print