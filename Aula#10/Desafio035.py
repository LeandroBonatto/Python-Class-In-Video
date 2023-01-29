print('-='*20)
print('Triangle Analyzer')
print('-='*20)
r1 = float(input('First segment: '))
r2 = float(input('Second segment: '))
r3 = float(input('Third segment: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
     print('The segments above CAN form a triangle!')
else:
     print('The segments above CANNOT form a triangle')


'''print('-='*20)
print('Analisador de Triangulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triangulo!')
else:
    print('Os segmentos acima NAO PODEM FORMAR triangulo')'''