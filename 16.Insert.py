colores = ['Rojo', 'Azul', 'Verde', 'Amarillo', 'Marron', 'Lila', 'Negro', 'Rosa', 'Blanco', 'Naranja']
mag = ('Magenta')
tur = ('Turquesa')
print ('A la lista:', colores, '\nSe le agregaran los colores:', mag, 'y', tur,'\n')
colores.insert(-4,mag)
colores.insert(-1,tur)
print ('\tLa lista quedaria de la siguiente manera:\n', colores)