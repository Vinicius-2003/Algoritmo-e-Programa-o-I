horatrab = int(input('Você trabalhou quantas horas este mês : '))
if horatrab > 160:
    if horatrab < 200:
        print('receberá 500R$ de bônus!')
    else:
        print('recebe 1000R$ de bônus!')
else:
    print('não haverá acréscimo ;-;')
if horatrab > 160:
    if horatrab < 200:
        print('Sua participação foi muito boa!')
    else:
        print('Sua participação foi ótima!')
else:
    print('Sua participação foi boa!')