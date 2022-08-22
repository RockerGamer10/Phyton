C=[]
cont=0
prom=0
Cant=int(input("Cuántos medidas de temperatura va a asignar? "))

for i in range (0, Cant):
    Temp=int(input("Temperatura: "))
    prom+=Temp
    C.append(Temp)

prom=prom/Cant

for i in range (0, Cant):
    if (C[i]>=prom):
        cont+=1

print(C)
print("Hay",cont,"mayores o iguales a la temperatura media")