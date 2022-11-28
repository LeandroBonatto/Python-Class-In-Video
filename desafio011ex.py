'''
# l = float(input('Qual a largura da parede: '))
# alt = float(input('Qual a altura da parede: '))
# area = l * alt
# t = (l * alt) / 2
# print('Sua parede tem a dimensao de {}x{} e sua area eh de {:.3f} m2.'.format(l, alt, area))
# print('Para pintar essa parede, vc precisara de {:.2f} litros de tinta.'.format(t)) #'''

wide = float(input('How wide is the wall: '))
tall = float(input('How tall is the wall: '))
area = wide * tall
total = (wide * tall) / 2
print('Your wall has the dimension of {}x{} and its area is {:.3f} m2.'.format(wide, tall, area))
print('To paint this wall, you will need {:.2f} liters of paint.'.format(total))