cont=int(0)
conf=1

print("Se calculara la cantidad de números primos hasta 1000")

for i in range (2,1000):
    conf=1
    for j in range (i-1,1,-1):
        if (i%j==0): conf=0
    if (conf==1): 
        print(i,"primo")
        cont+=1
print("Hay",cont,"primos")