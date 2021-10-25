#crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome santo. Usar o strip p eliminar os espaços, é importante!!!!
cidade = str(input('Digite o nome da sua cidade: ')).strip()
cidade = cidade.title()
split = cidade.split()
teste = 'Santo' in split[0]
print('Saiba se a sua cidade começa com o nome "Santo": {}'.format(teste))
print('Se True, começa; se False, nao começa.')
# print('Saiba se a sua cidade tem "santo" no nome: {}.'.format(split))