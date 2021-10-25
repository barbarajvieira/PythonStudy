#crie um programa que leia um numero e mostre se ele é par ou impar
n = int(input('Digite um número inteiro: '))
if n % 2 == 0:
    print('O numero {} é par!'.format(n))
else:
    print('O número {} é ímpar!'.format(n))