#faça um programa que leia uam frase pelo teclado e mostre: quantas vezes aparece a letra A, em que posição ela aparece pela 1a vez e em que posiçao aparece a ultima
frase = str(input('Digite uma frase: ')).strip()
frase2 = frase.upper()
counta = frase2.count('A')
print('Quantas vezes aparece a letra "A"? {}.'.format(counta))
find = frase2.find('A')
print('A posição em que a letra A aparece primeiro é: {}.'.format(find + 1))
find2 = frase2.rfind('A')
print('A posição em que a letra A aparece por último é: {}.'.format(find2 + 1))

# frase = str(input('Digite yma frase: ')).upper().strip()
# print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
# print('A primeira letra A apareceu na posição {}.'.format(frase.find('A') + 1))
# print('A última letra A apareceu na posiçao {}.'.format(frase.rfind('A') + 1))