entrada = input("Por favor, introduce un color iniciando con la primer letra en mayusculas:\n")
colores = ('Azul, Verde, Morado, Naranja')
if entrada in colores[0]:
    print('El color ',entrada, 'se esta dentro de nuestra lista\n')
elif entrada in colores[1]:
    print('El color ',entrada, 'se esta dentro de nuestra lista\n')
elif entrada in colores[2]:
    print('El color ',entrada, 'se esta dentro de nuestra lista\n')
elif entrada in colores[3]:
    print('El color ',entrada, 'se esta dentro de nuestra lista\n')
else:
    print('El color ',entrada, 'no se encuentra dentro de nuestra lista\n')
