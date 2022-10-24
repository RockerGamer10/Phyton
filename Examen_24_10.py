Zoologico=[]
Bucle=1
while (True):
    print("Presione 1 si desea agregar un animal a la lista")
    print("Presione 2 si desea eliminar un animal a la lista")
    print("Presione 3 si desea buscar un animal en la lista")
    print("Presione 0 si desea terminar el proceso y mostrar la lista")
    indice=(int(input()))
    if (indice==1):
        Zoologico.append(input("Animal a ingresar:"))
        Zoologico.sort()
    elif (indice==2):
        if (len(Zoologico)>0):
            for i in range (0,len(Zoologico)):
                print(i,Zoologico[i])
            num=int(input("Seleccione que eliminar:"))
            if(num<len(Zoologico) and num>=0):
                Zoologico.pop(num)
            else:
                print("No se encuentra")
        else:
            print("No hay animales en la lista")   
    elif (indice==3):
        if (len(Zoologico)>0):
            an=Zoologico.index(input("Animal a buscar:"))
            if (an==0 and len(Zoologico)==1):
                print("Es el único animal")
            elif (an==len(Zoologico)-1):
                print("A su izquierda esta ",Zoologico[an-1]+" y a la derecha nada, porque es el último")
            elif (an==0):
                print("A su izquierda no tiene nada, porque es el primero y a la derecha ",Zoologico[an+1])
            else:
                print("A su izquierda esta ",Zoologico[an-1]," y a la derecha ",Zoologico[an+1])
        else:
            print("No hay animales en la lista")   
    elif (indice==0):
        print(Zoologico)
        break
    else:
        print("Opción no valida.")