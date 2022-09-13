import math
r = int(input(' Me informe o raio da esfera (em cm) : '))
v = 4/3 * (math.pi) * (math.pow(r,3))
print('O valor do volume da esfera é de {:.2f}cm^3'.format(v))