'''
d = float(input('Digite uma distancia em metros: '))
print('medida de {:.1f}m corresponde a'.format(d))'''

d = float(input('Enter the distance in meters: '))
print('Measure of {:.1f}m is equivalent to'.format(d))
km = d / 1000
hm = d / 100
dam = d / 10
dm = d * 10
cm = d * 100
mm = d * 1000
print('{:.3f}km'.format(km))
print('{:.2f}hm'.format(hm))
print('{:.1f}dam'.format(dam))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))