#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
km = float(input('Qual a quantidade de km rodados? '))
d = int(input('Quantidade de dias do aluguel: '))
preco = (0.15 * km) + (60 * d)
print('O preço a pagar pelo aluguel do carro, rodando {} km por {} dias é de {:.2f} reais.'.format(km, d, preco))