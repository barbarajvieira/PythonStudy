#programa que leia o comprimento de 3 retas e diga ao usuario se elas podem ou nao formar um triangulo
r1 = float(input('comprimento da reta 1: '))
r2 = float(input('comprimento da reta 2: '))
r3 = float(input('comprimento da reta 3: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Analisando os comprimentos, é possível formar um triângulo!')
else:
    print('Analisando os comprimentos, nao é possível formar um triangulo!')