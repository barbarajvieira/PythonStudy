# Write a program that converts a value from meters to centimeters and millimeters
m = float(input('digite o valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
c = m * 100
mm = m * 1000

print('{}m é igual a: {}km, {}dam, {}hm, {}dm, {}cm e {}mm.'.format(m, km, hm, dam, dm, c, mm ))
