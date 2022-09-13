nota = int(input('Me informe a sua nota da prova (0 a 100): '))
if nota >= 90:
    print('Conceito A')
else:
    if nota < 90 and nota >= 80:
        print('Conceito B')
    elif nota < 80 and nota >= 70:
        print('Conceito C')
    elif nota < 70 and nota >= 60:
        print('Conceito D')
    else:
        print('Conceito E')
