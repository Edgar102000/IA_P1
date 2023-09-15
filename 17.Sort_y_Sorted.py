colores = ['Rojo', 'Azul', 'Verde', 'Amarillo', 'Marron', 'Lila', 'Negro', 'Rosa', 'Blanco', 'Naranja']
print ('La lista:', colores, '\nSera ordenada alfabeticamente de forma ascendente y descendente\n\tLa forma ascendente es:\n', sorted(colores))
colores.sort(reverse=True)
print('\n\tLa forma descendente es:\n',colores,'\n\tSabiendo que el primer color es el:',colores[0])
