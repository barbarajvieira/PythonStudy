# Write a program that converts brazilian real to dolar
brl = float(input('Quantos reais você quer converter para dólar?'))
usd = brl * 0.18
print('O valor convertido de {:.2f} reais é de {:.2f} dólares'. format(brl, usd))
