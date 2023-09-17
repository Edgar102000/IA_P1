print('Para la linea 4 se utilizan 4 argumentos.\nPara la linea 5 se utilizan 3 argumentos.\nPara la line 6 se utiliza un argumento.\nPara la linea 7 se utilizan 2 argumentos.\n')
def colores(*args):
	print('El color', args[0], 'es mi favorito.', 'El color', args[1], 'tampoco esta mal.')

colores('Verde','Azul')

def suma(*args):
	resultado=args[0] + args[1] + args[2] + args[3] + args[4]	
	print('\n\tLa suma de 5 numeros da como resultado:',resultado,'\n')	
suma(5,15,35,75,90)