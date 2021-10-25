#faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 > n2 and n1 > n3:
    print('{} é o maior numero.'.format(n1))
if n1 < n2 and n1 < n3:
    print('{} é o menor número.'.format(n1))
if n2 > n1 and n2 > n3:
    print('{} é o maior numero.'.format(n2))
if n2 < n1 and n2 < n3:
    print('{} é o menor número.'.format(n2))
if n3 > n1 and n3 > n2:
    print('{} é o maior número.'.format(n3))
if n3 < n1 and n3 < n2:
    print('{} é o menor número.'.format(n3))

#Resolução video
# n1 = int(input('Digite o primeiro numero: '))
# n2 = int(input('Digite o segundo numero: '))
# n3 = int(input('Digite o terceiro numero: '))
# menor = n1
# if n2 < n1 and n2 < n3:
#     menor = n2
# if n3 < n1 and n3 < n2:
#     menor = n3
# maior = n1
# if n2 > n1 and n2 > n3:
#     maior = n2
# if n3 > n1 and n3 > n2:
#     maior = n3
# print('O menor valor é {}.'.format(menor))
# print('O maior valor é {}.'.format(maior))