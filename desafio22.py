#programa q leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas, nome com tds as letras minusculas,
#quantas letras tem ao todo(sem considerar espaços), qts letras tem o primeiro nome
#a funçao strip elimina os espaços do começo e do fim
nome = str(input('Digite seu nome completo: ')).strip()
print('O seu nome em maiúsculas é: {}'.format(nome.upper()))
print('O seu nome em minúsculas é: {}'.format(nome.lower()))
print('O tamanho do seu nome é: {}'.format(len(nome) - nome.count(' ')))
nome = nome.split()
print('O seu primeiro nome tem o seguinte tamanho: {}'.format(len(nome[0])))

# count = 0
# for i in 'popo pupu':
#     if i != ' ':
#      count = count+1
#
# print(count)