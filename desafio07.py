# Write a program that receives 2 grades and do the average
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
avg = (n1+n2)/2
print('As notas do (a) aluno (a) sao {} e {}. Sua média é {:.2f}.'.format(n1, n2, avg))