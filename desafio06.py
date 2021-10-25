# Write a program that receives a number and do its double, triple and square root
n1 = int(input('digite um número: '))
d = n1 * 2
t = n1 * 3
sq = n1 ** (1/2)
print('O número que você digitou foi {}. Seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}.'.format(n1, d, t, sq))
