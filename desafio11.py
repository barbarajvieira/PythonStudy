# Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la (cada litro de tinta, pinta 2m2)
a = float(input('digite a altura da parede que deseja pintar (em metros):'))
l = float(input('digite a largura da parede que deseja pintar (em metros):'))
area = a * l
print('A altura da parede é de {} e a largura é de {}. A área total é de {} m2.'.format(a, l, area))
print('A quantidade de tinta para pintar toda a parede é de {} litros.'.format(area/2))