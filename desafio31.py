# faça um programa que pergunte a distancia de uma viagem em km. Calcule o preco da passagem cobrando 50 cents por km para viagens ate 200km e
# 45 cents o viagens mais longas
distancia = float(input('Qual a distância da sua viagem? '))
if distancia > 200:
    preco = distancia * 0.45
    print('Sua distancia é de {}km. O preço da sua passagem será: {:.2f} reais.'.format(distancia, preco))
else:
    preco = distancia * 0.5
    print('Sua distancia é de {}km. O preço da sua passagem será: {:.2f} reais.'.format(distancia, preco))

#maneira simplificada
# distancia = float(input('distancia da viagem: '))
# preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
# print('O preco da sua passagem é de: {:.2f}.'.format(preco))