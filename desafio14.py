#Converter temperatura celsius em fahrenheit
temp = float(input('Temperatura em Celsius: '))
f = (temp * 9/5) + 32
print('A temperatura de {} celsius corresponde a {:.2f} Fahrenheit.'.format(temp,f))