Monto=[]
suma=0
VMax=0
SMax=int

y=int(input("Ingrese la cantidad de años: "))
s=int(input("Ingrese la cantidad de sucursales: "))

for i in range (0,y):
    Monto.append([])
    for j in range (0, s):
        print("Monto del año",i+1,", sucursal número: ", j+1)
        Monto[i].append(int(input()))

for j in range (0,s):
    suma=0
    print("Sucursal",j+1)
    for i in range (0,y):
        suma+=Monto[i][j]
        if (suma>VMax):
            VMax=suma
            SMax=j
    print("La venta total fue de",suma)

print("La sucursal con mayor cantidad de ventas fue la número",SMax+1)

for i in range (0,y):
    prom=0
    YPMax=0
    for j in range (0,s):
        prom+=Monto[i][j]
    prom=prom/s
    print("Promedio del año",i+1,":",prom)
    if (prom>YPMax):
        YPMax=prom
        YMax=i

print("El año con mayor promedio de ventas fue el",YMax+1)