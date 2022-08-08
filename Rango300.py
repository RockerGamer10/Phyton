A1=int(1)
A2=int(0)
an=A1+(2*A2)
cont=int(1)

while (an<300):
    A2=A1
    A1=an
    an=A1+(2*A2)
    cont+=1
    print(an)

print("El rango es",cont,"y el primer número después de 300 es",an)