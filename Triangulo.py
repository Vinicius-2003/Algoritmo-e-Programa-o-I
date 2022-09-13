#parte 1
import math
cat = int(input(' Me informe o valor do cateto : '))
cat_oposto = int (input(' Me fale o valor do cateto oposto : '))
hipo = math.hypot(cat,cat_oposto)
print('O valor da hipotenusa é {:.0f} '.format(hipo))

#parte 2 
ang = float(input('Me fale o valor de um angulo (em graus) : '))
senang = math.sin(math.radians(ang))
cosang = math.cos(math.radians(ang))
tgsang = math.tan(math.radians(ang))
print ('O seno, cosseno e tangente do angulo escolhido, é respectivamente, {:.0f} ,{:.0f} , {:.0f}'.format(senang,cosang,tgsang))
