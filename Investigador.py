a = str(input("Telefonou para a vítima? : "))
b = str(input("Esteve no local do crime? : "))
c = str(input("Mora perto da vítima? : "))
d = str(input("Devia para a vítima? : "))
e = str(input("Já trabalhou com a vítima? : "))
if 's' > 'n':
    if 's' == 2:
        print('Suspeita')
    if ('s' == 3) or ('s' == 4):
        print('Cúmplice!')
    elif 's' == 5:
        print('Assassina')
else:
    print('Inocente')
