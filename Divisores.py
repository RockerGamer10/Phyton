print ("Ingrese un número, para finalizar, introduzca uno negativo")
num=int(input())
suma=int
while (num>0):
    suma=0
    for i in range(1,num):
        if (0==num%i): suma+=i
    suma+=num
    print ("La suma de sus divisores es",suma)
    num=int(input())
