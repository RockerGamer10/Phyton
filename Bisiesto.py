print("Ingrese el año")
año=int(input())
conf=año%4

if (conf==0):
    print("Es bisiesto")
else: print("No es bisiesto")