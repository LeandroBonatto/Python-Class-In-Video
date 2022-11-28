'''
# Largura = float(input('Qual a largura? '))
# Altura = float(input('Qual a altura? '))
# Quarto = Largura * Altura
# Area = Quarto / 2
# print('Para pintar um determinado quarto de {}m2, necessitamos de {} litros de tinta.'.format(Quarto, Area))'''

Width = float(input('How wide is it? '))
Height = float(input('How tall is it? '))
Bedroom = Width * Height
Area = Bedroom / 2
print('To paint a certain room of {:.2f} m2, we need {:.2f} liters of paint.'.format(Bedroom, Area))
