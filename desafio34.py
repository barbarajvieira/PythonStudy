#programa que pergunta o salario de um funcionario e calcule o valor de seu aumento.
# para salarios superiores a 1250, aumento de 10%. Para inferiores, aumento de 15%
salario = float(input('Qual o seu salário? '))
if salario <= 1250:
    print('O seu aumento é de 15%. Seu novo salário será: {:.2f} reais.'.format(salario*1.15))
else:
    print('O seu aumento é de 10%. Seu novo salário é: {:.2f} reais.'.format(salario*1.1))

# salario = float(input('Qual o salario? '))
# if salario <= 1250:
#     novo = salario * 1.15
# else:
#     novo = salario *1.1
# print('quem ganhava {:.2f} passa a ganhar {:.2f}.'.format(salario, novo))