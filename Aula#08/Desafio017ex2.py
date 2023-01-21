from math import hypot
co = float(input('Enter a value for the opposite side: '))
ca = float(input('Enter a value for the Adjacent Leg: '))
hypo = (co ** 2 + ca ** 2) ** (1/2)
print('Hypotenuse value will be {:.2f}'.format(hypo))

'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''