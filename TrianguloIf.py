a = int(input('Me fale um valor : '))
b = int(input('Me fale outro valor : '))
c = int(input('Me fale um ultimo valor : '))
if (a < b + c) and (b < a + c) and (c < a + b):
    if a == b and b == c:
        print('É um triangulo equilátero!')
    elif a == b or b == c :
        print('É um triangulo isósceles!')
    else:
        print('É um triangulo escaleno!')
else:
    print('Não formará um triangulo !')

    #if (a > b + c) and (b > a + c) and (c > a + b):
    #print('Não formará um triangulo!')
#else:
    #if a == b and b == c:
        #print('É um triangulo equilátero!')
    #elif a == b or b ==c :
        #print('É um triangulo isósceles!')
    #elif a != b and b!=c and a!=c:
        #print('É um triangulo escaleno!')