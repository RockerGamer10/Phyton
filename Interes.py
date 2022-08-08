cap=0
gain=0
year=-1

print("Ingrese el capital, la tasa de interés, y la cantidad de años")
print("Todo mayor que 0")
print("Intereses menor a 100")

while (cap<1): cap=int(input())
capF=float(cap)
while (year<0): year=int(input())
while (gain<0 | gain>100): gain=int(input())
rate=float(gain*0.01)

for i in range(year):
    capF=capF*rate
print("El dinero obtenido al final es",capF)