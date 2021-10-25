# escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma msg dizendo que ele foi multado.
# A multa vai custar 7 reais por cada km acima do limite
v = float(input('Qual a velocidade atual do seu carro? '))
if v > 80:
    m = (v - 80) * 7
    print('Sua velocidade é de {} km/h e está acima do permitido! Você foi multado! O valor da sua multa é de: BRL {:.2f}.'.format(v,m))
else:
    print('Sua velocidade é de {} km/h e está dentro do limite.'.format(v))
    print('Tenha um bom dia e dirija em segyurança!')