import random

lista=[]

cant=int(input("Cantidad de números: "))

for i in range (0, cant):
    num=random.randint(1,100)
    lista.append(num)

lista.sort()
num=0

for i in range (0, cant):
    if (lista[i]>num):
        print(lista[i])
        num=lista[i]