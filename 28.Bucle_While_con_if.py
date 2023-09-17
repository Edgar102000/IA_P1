x=0
while x<=30:
    x +=1

    if x==15:
        print("La ejecucion del bucle se ha quebrado cuando el valor de x fue:",x)
        break

    if x==4 or x==6 or x==10:
        print("Se salto el valor de",x,"de x")
        continue
    print (x)
