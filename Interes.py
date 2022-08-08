cap=-1
gain=-1
year=-1

print("Ingrese el capital, la tasa de interés, y la cantidad de años")
print("Todo mayor que 0")
print("Intereses menor a 100")

while (cap<1): cap=int(input())
capF=float(cap)
while (gain<0 or gain>100): gain=int(input())

while (year<0): year=int(input())
rate=float((gain*0.01)+1)

for i in range(year):
    capF=capF*rate
print("El dinero obtenido al final es",capF)