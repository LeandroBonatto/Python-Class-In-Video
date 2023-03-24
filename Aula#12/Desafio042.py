r1 = float(input('First segment: '))
r2 = float(input('Second segment: '))
r3 = float(input('Third segment: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
     print('The segments above CAN FORM a triangle ', end='')
     if r1 == r2 == r3:
         print('EQUILATERO!')
     elif r1 != r2 != r3 != r1:
         print('ESCALENO!')
     else:
         print('ISOSCELES!')
else:
     print('The segments above CANNOT form a triangle')


'''r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print('Os segmentos acima NAO PODEM FORMAR um triangulo')'''