print("Ingrese un número entre 0 y 10")
num=int(input())

if (num>0 & num<11):
    conf=num%2
    if (conf==0):
        print("PAR")
    else: print("IMPAR")
else: print("Fuera de rango")